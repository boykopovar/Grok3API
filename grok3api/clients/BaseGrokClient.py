from typing import Dict, Optional, Tuple, Type, AsyncIterator

from curl_cffi.requests import AsyncSession

from grok3api.types import ResponseChunk, TokenChunk
from grok3api.types.exceptions.handle import raise_for_rest, raise_for_grpc
from grok3api.utils.api.anon_session import DEFAULT_ANON_HEADERS, AnonCredential, generate_anon_credential
from grok3api.utils.constants import (
    BASE_URL,
)
from grok3api.utils.parse_response import parse_chunk
from grok3api.utils.protobuf import (
    grpc_frame,
)


class BaseGrokClient:
    def __init__(
        self,
        credential: Optional[AnonCredential],
        timeout: int,
        ssl: bool,
        connector_limit: int,
    ) -> None:
        self._credential = credential
        self._timeout = timeout
        self._ssl = ssl
        self._connector_limit = connector_limit

        self._session: Optional[AsyncSession] = None

    async def __aenter__(self) -> "BaseGrokClient":
        await self.open()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()

    @property
    def credential(self) -> Optional[AnonCredential]:
        return self._credential

    @property
    def is_open(self) -> bool:
        return self._session is not None

    def _create_session(self) -> AsyncSession:
        return AsyncSession(
            impersonate="chrome131_android",
            timeout=self._timeout,
            verify=self._ssl,
        )

    async def open(self) -> None:
        if self.is_open:
            return

        self._session = self._create_session()

        await self.create_anonymous_account()

    async def close(self) -> None:
        if self._session is not None:
            await self._session.close()
            self._session = None

    def _ensure_session(self) -> None:
        assert self._session is not None

    def _ensure_credentials(self):
        assert self._credential is not None

    @staticmethod
    def _build_headers(
            extra: Optional[Dict[str, str]] = None
    ) -> Dict[str, str]:
        if extra:
            headers = (
                DEFAULT_ANON_HEADERS.copy()
            )
            headers.update(extra)
            return headers

        return DEFAULT_ANON_HEADERS.copy()


    async def _stream(
            self,
            endpoint: str,
            payload: bytes,
            skip_thinking: bool,
            chunks_white_list: Optional[Tuple[Type[ResponseChunk], ...]],
    ) -> AsyncIterator[ResponseChunk]:
        self._ensure_session()
        self._ensure_credentials()

        buffer = bytearray()

        async with self._session.stream(
                "POST",
                BASE_URL + endpoint,
                data=grpc_frame(payload),
                headers=self._build_headers(self._credential.headers),
        ) as response:
            if response.status_code != 200:
                await raise_for_rest(response)

            async for chunk in response.aiter_content():
                buffer.extend(chunk)

                while True:
                    if len(buffer) < 5:
                        break

                    frame_length = int.from_bytes(buffer[1:5], "big")
                    total = 5 + frame_length

                    if len(buffer) < total:
                        break

                    frame_body = bytes(buffer[5:total])
                    del buffer[:total]

                    for parsed_chunk in parse_chunk(frame_body):
                        if (
                                skip_thinking and isinstance(parsed_chunk, TokenChunk) and
                                parsed_chunk.is_thinking
                        ):
                            continue

                        if chunks_white_list and not isinstance(parsed_chunk, chunks_white_list):
                            continue

                        yield parsed_chunk

            raise_for_grpc(response)


    async def create_anonymous_account(
        self,
    ) -> AnonCredential:
        self._ensure_session()

        credential: AnonCredential = await generate_anon_credential(self._session)

        self._credential = credential

        return credential

    async def ensure_authorized(
        self,
    ) -> None:
        if self._credential is None:
            await self.create_anonymous_account()
