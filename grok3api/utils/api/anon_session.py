import base64
import hashlib
import struct
from dataclasses import dataclass
from typing import Dict, Union, List

from aiohttp import ClientSession
from coincurve import PrivateKey

from grok3api.types.exceptions.handle import raise_for_rest, raise_for_grpc
from grok3api.utils.constants import (
    APP_VERSION,
    BASE_URL,
    GRPC_CREATE_ANON_CHALLENGE,
    GRPC_CREATE_ANON_USER,
)
from grok3api.utils.protobuf import (
    grpc_frame,
    pb_bytes,
    pb_parse,
    pb_str,
)

DEFAULT_ANON_HEADERS: Dict[
    str,
    Union[str, Dict[str, str]],
] = {
    "Content-Type": "application/grpc+proto",
    "Accept": "application/grpc+proto",
    "TE": "trailers",
    "User-Agent": (
        f"grpc-java-okhttp/1.65.1 "
        f"ai.x.grok/{APP_VERSION} "
        f"(Android; okhttp/4.12.0)"
    ),
}

@dataclass(frozen=True)
class AnonCredential:
    anon_user_id: str
    challenge_b64: str
    signature_b64: str

    @property
    def headers(self) -> Dict[str, str]:
        return {
            "x-anonuserid": self.anon_user_id,
            "x-challenge": self.challenge_b64,
            "x-signature": self.signature_b64,
        }


def _grpc_unframe(raw: bytes) -> List[bytes]:
    frames: List[bytes] = []

    pos: int = 0

    while pos + 5 <= len(raw):
        length: int = struct.unpack(
            ">I",
            raw[pos + 1:pos + 5],
        )[0]

        pos += 5

        frames.append(
            raw[pos:pos + length],
        )

        pos += length

    return frames


async def _anon_unary(
        session: ClientSession,
        method: str,
        payload: bytes,
) -> bytes:
    async with session.post(
        BASE_URL + method,
        data=grpc_frame(payload),
        headers=DEFAULT_ANON_HEADERS.copy(),
    ) as response:
        raw: bytes = await response.read()
        raise_for_grpc(response)

        if response.status != 200:
            await raise_for_rest(response)

        return _grpc_unframe(raw)[0]


async def generate_anon_credential(
        session: ClientSession,
) -> AnonCredential:
    private_key: PrivateKey = PrivateKey()

    public_key: bytes = private_key.public_key.format(
        compressed=True,
    )

    payload: bytes = await _anon_unary(
        session,
        GRPC_CREATE_ANON_USER,
        pb_bytes(1, public_key),
    )

    anon_user_id: str = pb_parse(payload)[1][0].decode()

    payload = await _anon_unary(
        session,
        GRPC_CREATE_ANON_CHALLENGE,
        pb_str(1, anon_user_id),
    )

    challenge: bytes = pb_parse(payload)[1][0]

    digest: bytes = hashlib.sha256(challenge).digest()

    signature: bytes = private_key.sign_recoverable(
        digest,
        hasher=None,
    )[:64]

    return AnonCredential(
        anon_user_id=anon_user_id,
        challenge_b64=base64.b64encode(challenge).decode(),
        signature_b64=base64.b64encode(signature).decode(),
    )