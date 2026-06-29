from __future__ import annotations

import asyncio
import base64
import datetime
import hashlib
import random
import secrets
import struct
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import coincurve
import curl_cffi
from aiohttp import ClientSession
from curl_cffi import requests as cffi_requests, AsyncSession

from grok3api.utils.api.anon_session import AnonCredential, generate_anon_credential

HOST: str = "accounts.x.ai"
GRPC_BASE: str = f"https://{HOST}"
SERVICE_PATH: str = "/auth_frontend.AuthFrontend"
USER_AGENT: str = "grpc-java-okhttp/1.67.0-SNAPSHOT"
CONTENT_TYPE: str = "application/grpc"
TOS_VERSION: int = 5
REQUEST_TIMEOUT: int = 15
CONNECT_TIMEOUT: int = 10

_STEP_KEYGEN: str = "keygen"
_STEP_SIGN: str = "sign"
_STEP_REGISTER: str = "register"
_STEP_CREATE_ANON: str = "CreateAnonUser"
_STEP_CHALLENGE: str = "CreateAnonUserChallenge"
_STEP_SESSION: str = "CreateSession"
_STEP_BIRTH: str = "SetBirthDate"
_STEP_TOS: str = "SetTosAcceptedVersion"

_MSG_RESPONSE_PAYLOAD: str = "response payload"
_MSG_RESPONSE_EMPTY: str = "response (empty expected)"
_MSG_BYTES_HEX: str = "bytes hex"
_MSG_NOT_FOUND: str = "not found in response"
_MSG_WIRE_TYPE: str = "Unknown wire type"
_MSG_AT_TAG: str = "at tag"
_MSG_CONNECTING: str = "connecting..."

_HDR_CONTENT_TYPE: str = "content-type"
_HDR_ENCODING: str = "grpc-encoding"
_HDR_UA: str = "user-agent"
_HDR_TE: str = "te"
_HDR_ANON_ID: str = "x-anonuserid"
_HDR_CHALLENGE: str = "x-challenge"
_HDR_SIGNATURE: str = "x-signature"

_WIRE_LEN: int = 2
_WIRE_VARINT: int = 0
_WIRE_64: int = 1
_WIRE_32: int = 5

_PACK_FRAME: str = ">BI"
_SFX_BYTES: str = " bytes"


def _log(step: str, msg: str) -> None:
    print(f"[{step}] {msg}", flush=True)


def _encode_grpc_frame(body: bytes) -> bytes:
    return struct.pack(_PACK_FRAME, 0, len(body)) + body


def _decode_grpc_frame(data: bytes) -> bytes:
    if len(data) < 5:
        raise ValueError(f"gRPC frame too short: {len(data)}{_SFX_BYTES}")
    compressed, length = struct.unpack(_PACK_FRAME, data[:5])
    if compressed != 0:
        raise ValueError(f"Unexpected compressed flag: {compressed}")
    payload: bytes = data[5:5 + length]
    if len(payload) != length:
        raise ValueError(f"Frame length mismatch: expected {length}, got {len(payload)}")
    return payload


def _encode_varint(value: int) -> bytes:
    parts: List[int] = []
    while value > 0x7F:
        parts.append((value & 0x7F) | 0x80)
        value >>= 7
    parts.append(value & 0x7F)
    return bytes(parts)


def _decode_varint(data: bytes, pos: int) -> Tuple[int, int]:
    result: int = 0
    shift: int = 0
    while pos < len(data):
        byte: int = data[pos]
        pos += 1
        result |= (byte & 0x7F) << shift
        if not (byte & 0x80):
            return result, pos
        shift += 7
    raise ValueError("Varint terminated unexpectedly")


def _encode_len_field(tag: int, value: bytes) -> bytes:
    key: bytes = _encode_varint((tag << 3) | _WIRE_LEN)
    return key + _encode_varint(len(value)) + value


def _encode_string_field(tag: int, value: str) -> bytes:
    return _encode_len_field(tag, value.encode())


def _encode_bytes_field(tag: int, value: bytes) -> bytes:
    return _encode_len_field(tag, value)


def _encode_int32_field(tag: int, value: int) -> bytes:
    key: bytes = _encode_varint((tag << 3) | _WIRE_VARINT)
    return key + _encode_varint(value)


def _encode_bool_field(tag: int, value: bool) -> bytes:
    return _encode_int32_field(tag, 1 if value else 0)


def _decode_field_bytes(data: bytes, expected_tag: int) -> bytes:
    pos: int = 0
    while pos < len(data):
        key_val, pos = _decode_varint(data, pos)
        wire_type: int = key_val & 0x7
        tag: int = key_val >> 3
        if wire_type == _WIRE_LEN:
            length, pos = _decode_varint(data, pos)
            chunk: bytes = data[pos:pos + length]
            pos += length
            if tag == expected_tag:
                return chunk
        elif wire_type == _WIRE_VARINT:
            _, pos = _decode_varint(data, pos)
        elif wire_type == _WIRE_64:
            pos += 8
        elif wire_type == _WIRE_32:
            pos += 4
        else:
            raise ValueError(f"{_MSG_WIRE_TYPE} {wire_type} {_MSG_AT_TAG} {tag}")
    raise ValueError(f"tag={expected_tag} {_MSG_NOT_FOUND}")


def _decode_string_field(data: bytes, expected_tag: int) -> str:
    return _decode_field_bytes(data, expected_tag).decode()


def _decode_nested_field(data: bytes, expected_tag: int) -> bytes:
    return _decode_field_bytes(data, expected_tag)


@dataclass
class AnonKeys:
    private_key: bytes
    public_key_compressed: bytes


@dataclass
class AnonUser:
    anon_user_id: str


@dataclass
class Challenge:
    challenge_bytes: bytes



@dataclass
class Session:
    session_id: str
    session_cookie: str


def _base_headers() -> Dict[str, str]:
    return {
        _HDR_CONTENT_TYPE: CONTENT_TYPE,
        _HDR_ENCODING: "identity",
        _HDR_UA: USER_AGENT,
        _HDR_TE: "trailers",
    }


def _auth_headers(creds: AnonCredential) -> Dict[str, str]:
    h: Dict[str, str] = _base_headers()
    h[_HDR_ANON_ID] = creds.anon_user_id
    h[_HDR_CHALLENGE] = creds.challenge_b64
    h[_HDR_SIGNATURE] = creds.signature_b64
    return h


def _grpc_post(
    session: cffi_requests.Session,
    method: str,
    proto_body: bytes,
    headers: Dict[str, str],
) -> bytes:
    url: str = f"{GRPC_BASE}{SERVICE_PATH}/{method}"
    frame: bytes = _encode_grpc_frame(proto_body)
    _log(method, f"POST {url} — frame {len(frame)}{_SFX_BYTES} — {_MSG_CONNECTING}")
    resp = session.post(
        url,
        data=frame,
        headers=headers,
        http_version=2,
        timeout=(CONNECT_TIMEOUT, REQUEST_TIMEOUT),
    )
    _log(method, f"HTTP {resp.status_code}")
    if resp.status_code != 200:
        raise RuntimeError(f"{method} failed HTTP {resp.status_code}: {resp.text[:300]}")
    grpc_status: Optional[str] = resp.headers.get("grpc-status")
    grpc_message: Optional[str] = resp.headers.get("grpc-message")
    _log(method, f"grpc-status={grpc_status} grpc-message={grpc_message}")
    if grpc_status is not None and grpc_status != "0":
        raise RuntimeError(f"{method} gRPC error {grpc_status}: {grpc_message}")
    return _decode_grpc_frame(resp.content)


def _log_payload(step: str, payload: bytes) -> None:
    _log(step, f"{_MSG_RESPONSE_PAYLOAD} {len(payload)} {_MSG_BYTES_HEX}: {payload.hex()}")


def _log_empty(step: str, payload: bytes) -> None:
    _log(step, f"{_MSG_RESPONSE_EMPTY} {len(payload)} bytes: {payload.hex()}")


def step_generate_keys() -> AnonKeys:
    _log(_STEP_KEYGEN, "Generating secp256k1 keypair")
    priv: bytes = secrets.token_bytes(32)
    pk = coincurve.PrivateKey(priv)
    compressed: bytes = pk.public_key.format(compressed=True)
    _log(_STEP_KEYGEN, f"private_key={priv.hex()}")
    _log(_STEP_KEYGEN, f"public_key_compressed={compressed.hex()} ({len(compressed)}{_SFX_BYTES})")
    return AnonKeys(private_key=priv, public_key_compressed=compressed)


def step_create_anon_user(
    session: cffi_requests.Session,
    keys: AnonKeys,
) -> AnonUser:
    _log(_STEP_CREATE_ANON, "Sending CreateAnonUserRequest")
    proto_body: bytes = _encode_bytes_field(1, keys.public_key_compressed)
    payload: bytes = _grpc_post(session, _STEP_CREATE_ANON, proto_body, _base_headers())
    _log_payload(_STEP_CREATE_ANON, payload)
    anon_user_id: str = _decode_string_field(payload, 1)
    _log(_STEP_CREATE_ANON, f"anon_user_id={anon_user_id}")
    return AnonUser(anon_user_id=anon_user_id)


def step_create_challenge(
    session: cffi_requests.Session,
    anon_user: AnonUser,
) -> Challenge:
    _log(_STEP_CHALLENGE, f"Requesting challenge for anon_user_id={anon_user.anon_user_id}")
    proto_body: bytes = _encode_string_field(1, anon_user.anon_user_id)
    payload: bytes = _grpc_post(session, _STEP_CHALLENGE, proto_body, _base_headers())
    _log_payload(_STEP_CHALLENGE, payload)
    challenge_bytes: bytes = _decode_field_bytes(payload, 1)
    _log(_STEP_CHALLENGE, f"challenge_bytes={challenge_bytes.hex()} ({len(challenge_bytes)}{_SFX_BYTES})")
    return Challenge(challenge_bytes=challenge_bytes)


def step_build_credentials(
    anon_user: AnonUser,
    keys: AnonKeys,
    challenge: Challenge,
) -> AnonCredential:
    _log(_STEP_SIGN, "Computing SHA-256 of challenge bytes")
    digest: bytes = hashlib.sha256(challenge.challenge_bytes).digest()
    _log(_STEP_SIGN, f"sha256(challenge)={digest.hex()}")
    pk = coincurve.PrivateKey(keys.private_key)
    sig: bytes = pk.sign_recoverable(digest, hasher=None)[:64]
    _log(_STEP_SIGN, f"signature={sig.hex()} ({len(sig)}{_SFX_BYTES}, compact r||s)")
    challenge_b64: str = base64.b64encode(challenge.challenge_bytes).decode()
    signature_b64: str = base64.b64encode(sig).decode()
    _log(_STEP_SIGN, f"x-challenge={challenge_b64}")
    _log(_STEP_SIGN, f"x-signature={signature_b64}")
    return AnonCredential(
        anon_user_id=anon_user.anon_user_id,
        challenge_b64=challenge_b64,
        signature_b64=signature_b64,
    )


def step_create_session(
    session: cffi_requests.Session,
    creds: AnonCredential,
    email: str,
    password: str,
) -> Session:
    _log(_STEP_SESSION, f"Creating session for email={email}")
    email_pw_body: bytes = _encode_string_field(1, email) + _encode_string_field(2, password)
    credentials_field: bytes = _encode_bytes_field(1, email_pw_body)
    proto_body: bytes = (
        credentials_field
        + _encode_string_field(7, creds.anon_user_id)
        + _encode_bool_field(8, False)
    )
    payload: bytes = _grpc_post(session, _STEP_SESSION, proto_body, _auth_headers(creds))
    _log_payload(_STEP_SESSION, payload)
    outer: bytes = _decode_nested_field(payload, 1)
    session_nested: bytes = _decode_nested_field(outer, 1)
    session_id: str = _decode_string_field(session_nested, 1)
    session_cookie: str = _decode_string_field(outer, 2)
    _log(_STEP_SESSION, f"session_id={session_id}")
    _log(_STEP_SESSION, f"session_cookie={session_cookie[:40]}...")
    return Session(session_id=session_id, session_cookie=session_cookie)


def step_set_birth_date(
    session: cffi_requests.Session,
    creds: AnonCredential,
    birth_unix: int,
) -> None:
    _log(_STEP_BIRTH, f"Setting birth date unix={birth_unix}")
    ts_body: bytes = _encode_int32_field(1, birth_unix)
    proto_body: bytes = _encode_bytes_field(1, ts_body)
    payload: bytes = _grpc_post(session, _STEP_BIRTH, proto_body, _auth_headers(creds))
    _log_empty(_STEP_BIRTH, payload)


def step_set_tos(
    session: cffi_requests.Session,
    creds: AnonCredential,
) -> None:
    _log(_STEP_TOS, f"Accepting ToS version={TOS_VERSION}")
    proto_body: bytes = _encode_int32_field(2, TOS_VERSION)
    payload: bytes = _grpc_post(session, _STEP_TOS, proto_body, _auth_headers(creds))
    _log_empty(_STEP_TOS, payload)


async def register(email: str, password: str, birth_unix: int) -> Session:
    http_session: cffi_requests.Session = cffi_requests.Session()
    async_session = AsyncSession(impersonate="chrome131_android")
    creds: AnonCredential = await generate_anon_credential(async_session)
    sess: Session = step_create_session(http_session, creds, email, password)
    step_set_birth_date(http_session, creds, birth_unix)
    step_set_tos(http_session, creds)
    _log(_STEP_REGISTER, f"Done. session_id={sess.session_id}")
    return sess


def _random_adult_birth_unix() -> int:
    today: datetime.date = datetime.date.today()
    min_year: int = today.year - 40
    max_year: int = today.year - 20
    year: int = random.randint(min_year, max_year)
    month: int = random.randint(1, 12)
    max_day: int = (datetime.date(year + (month // 12), (month % 12) + 1, 1) - datetime.timedelta(days=1)).day
    day: int = random.randint(1, max_day)
    dt: datetime.datetime = datetime.datetime(year, month, day, tzinfo=datetime.timezone.utc)
    return int(dt.timestamp())


def _read_password() -> str:
    sys.stderr.write("Password: ")
    sys.stderr.flush()
    return sys.stdin.readline().rstrip("\n")


def _prompt_credentials() -> Tuple[str, str]:
    argc: int = len(sys.argv)
    email: str = sys.argv[1] if argc > 1 else input("Email: ")
    password: str = sys.argv[2] if argc > 2 else _read_password()
    return email, password


async def main() -> None:
    _email, _password = _prompt_credentials()
    _birth_unix: int = _random_adult_birth_unix()
    _birth_date: datetime.date = datetime.datetime.utcfromtimestamp(_birth_unix).date()
    print(f"[main] Using birth date: {_birth_date} (unix={_birth_unix})")
    result: Session = await register(
        email=_email,
        password=_password,
        birth_unix=_birth_unix,
    )
    print(f"\nResult:")
    print(f"  session_id:     {result.session_id}")
    print(f"  session_cookie: {result.session_cookie}")


if __name__ == "__main__":
    asyncio.run(main())
