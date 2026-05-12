import base64
import hashlib
import struct
from dataclasses import dataclass
from typing import Dict, Optional, Union, List

from aiohttp import ClientSession, ClientTimeout, TCPConnector
from coincurve import PrivateKey

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

_DEFAULT_ANON_HEADERS: Dict[
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


class BaseGrokClient:
    def __init__(
        self,
        credential: Optional[
            AnonCredential
        ] = None,
        timeout: int = 120,
        ssl: bool = True,
        connector_limit: int = 100,
    ) -> None:
        self._credential = credential
        self._timeout = timeout
        self._ssl = ssl
        self._connector_limit = connector_limit

        self._connector: Optional[
            TCPConnector
        ] = None

        self._session: Optional[
            ClientSession
        ] = None

    async def __aenter__(
        self,
    ) -> "BaseGrokClient":
        await self.open()
        return self

    async def __aexit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> None:
        await self.close()

    @property
    def session(self) -> ClientSession:
        if self._session is None:
            raise RuntimeError(
                "Client session is not opened",
            )

        return self._session

    @property
    def credential(
        self,
    ) -> Optional[AnonCredential]:
        return self._credential

    @property
    def is_open(self) -> bool:
        return (
            self._session is not None
            and not self._session.closed
        )

    async def open(self) -> None:
        if self.is_open:
            return

        self._connector = TCPConnector(
            ssl=self._ssl,
            limit=self._connector_limit,
        )

        self._session = ClientSession(
            timeout=ClientTimeout(
                total=self._timeout,
            ),
            connector=self._connector,
        )

    async def close(self) -> None:
        if self._session is not None:
            await self._session.close()
            self._session = None

        if self._connector is not None:
            await self._connector.close()
            self._connector = None

    async def _ensure_session(
        self,
    ) -> None:
        if not self.is_open:
            await self.open()

    @staticmethod
    def build_headers(
        extra: Optional[
            Dict[str, str]
        ] = None,
    ) -> Dict[str, str]:
        if extra:
            headers = (
                _DEFAULT_ANON_HEADERS.copy()
            )

            headers.update(extra)

            return headers

        return _DEFAULT_ANON_HEADERS.copy()

    @staticmethod
    def grpc_unframe(
        raw: bytes,
    ) -> List[bytes]:
        frames = []

        pos = 0

        while pos + 5 <= len(raw):
            length = struct.unpack(
                ">I",
                raw[pos + 1:pos + 5],
            )[0]

            pos += 5

            frames.append(
                raw[pos:pos + length],
            )

            pos += length

        return frames

    async def grpc_unary(
        self,
        method: str,
        payload: bytes,
        headers: Optional[
            Dict[str, str]
        ] = None,
    ) -> bytes:
        await self._ensure_session()

        async with self.session.post(
            BASE_URL + method,
            data=grpc_frame(payload),
            headers=self.build_headers(
                headers,
            ),
        ) as response:
            raw = await response.read()

            grpc_status = response.headers.get(
                "grpc-status",
                "0",
            )

            if grpc_status != "0":
                raise RuntimeError(
                    "gRPC {}: {}".format(
                        grpc_status,
                        response.headers.get(
                            "grpc-message",
                            "?",
                        ),
                    ),
                )

            if response.status != 200:
                raise RuntimeError(
                    "HTTP {}".format(
                        response.status,
                    ),
                )

            return self.grpc_unframe(
                raw,
            )[0]

    async def create_anonymous_account(
        self,
    ) -> AnonCredential:
        private_key = PrivateKey()

        public_key = (
            private_key.public_key.format(
                compressed=True,
            )
        )

        payload = await self.grpc_unary(
            GRPC_CREATE_ANON_USER,
            pb_bytes(1, public_key),
        )

        anon_user_id = pb_parse(
            payload,
        )[1][0].decode()

        payload = await self.grpc_unary(
            GRPC_CREATE_ANON_CHALLENGE,
            pb_str(1, anon_user_id),
        )

        challenge = pb_parse(
            payload,
        )[1][0]

        digest = hashlib.sha256(
            challenge,
        ).digest()

        signature = (
            private_key.sign_recoverable(
                digest,
                hasher=None,
            )[:64]
        )

        credential = AnonCredential(
            anon_user_id=anon_user_id,
            challenge_b64=base64.b64encode(
                challenge,
            ).decode(),
            signature_b64=base64.b64encode(
                signature,
            ).decode(),
        )

        self._credential = credential

        return credential

    async def ensure_authorized(
        self,
    ) -> None:
        if self._credential is None:
            await self.create_anonymous_account()