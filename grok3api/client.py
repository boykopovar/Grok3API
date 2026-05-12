from typing import AsyncIterator

from grok3api.clients.BaseGrokClient import BaseGrokClient
from grok3api.types import (
    AskResponse,
    ConversationChunk,
    FinalMetadataChunk,
    ModelResponseChunk,
    ResponseChunk,
    SurveyChunk,
    TitleChunk,
    TokenChunk,
)
from grok3api.types.request import ChatRequest
from grok3api.utils.constants import BASE_URL, GRPC_CHAT
from grok3api.utils.parse_response import parse_chunk
from grok3api.utils.protobuf import grpc_frame


class GrokClient(BaseGrokClient):
    async def ask_stream(
        self,
        request: ChatRequest,
    ) -> AsyncIterator[ResponseChunk]:
        await self._ensure_session()
        await self.ensure_authorized()

        assert self._session is not None
        assert self._credential is not None

        async with self._session.post(
            BASE_URL + GRPC_CHAT,
            data=grpc_frame(request.encode()),
            headers=self.build_headers(
                self._credential.headers,
            ),
        ) as response:
            if response.status != 200:
                body = await response.read()

                raise RuntimeError(
                    "HTTP {}: {}".format(
                        response.status,
                        body,
                    ),
                )

            buffer = bytearray()

            async for chunk in response.content.iter_any():
                buffer.extend(chunk)

                while True:
                    if len(buffer) < 5:
                        break

                    frame_length = int.from_bytes(
                        buffer[1:5],
                        "big",
                    )

                    total = 5 + frame_length

                    if len(buffer) < total:
                        break

                    frame_body = bytes(
                        buffer[5:total],
                    )

                    del buffer[:total]

                    for parsed_chunk in parse_chunk(
                        frame_body,
                    ):
                        yield parsed_chunk

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

    async def ask(
        self,
        request: ChatRequest,
    ) -> AskResponse:
        tokens = []

        result = AskResponse(text="")

        async for chunk in self.ask_stream(
            request,
        ):
            if isinstance(chunk, TokenChunk):
                if (
                    chunk.is_final
                    and chunk.token
                ):
                    tokens.append(chunk.token)

            elif isinstance(
                chunk,
                ModelResponseChunk,
            ):
                result.model_response = (
                    chunk.model_response
                )

            elif isinstance(
                chunk,
                FinalMetadataChunk,
            ):
                result.final_metadata = (
                    chunk.final_metadata
                )

            elif isinstance(chunk, SurveyChunk):
                result.survey = chunk.survey

            elif isinstance(
                chunk,
                ConversationChunk,
            ):
                result.conversation = (
                    chunk.conversation
                )

            elif isinstance(chunk, TitleChunk):
                result.title = chunk.new_title

        result.text = "".join(tokens)

        return result