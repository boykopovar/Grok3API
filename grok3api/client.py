from typing import AsyncIterator, Optional, Type, Tuple

from grok3api.clients.BaseGrokClient import BaseGrokClient, AnonCredential
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
    def __init__(
            self,
            credential: Optional[AnonCredential] = None,
            timeout: int = 120,
            ssl: bool = True,
            connector_limit: int = 100,
    ) -> None:
        super().__init__(
            credential=credential,
            timeout=timeout,
            ssl=ssl,
            connector_limit=connector_limit,
        )

    async def ask_stream(
            self,
            request: ChatRequest,
            skip_thinking: bool = True,
            chunks_white_list: Optional[Tuple[Type[ResponseChunk], ...]] = (TokenChunk, )
    ) -> AsyncIterator[ResponseChunk]:
        self._ensure_session()
        self._ensure_credentials()

        async with self._session.post(
                BASE_URL + GRPC_CHAT,
                data=grpc_frame(request.encode()),
                headers=self._build_headers(
                    self._credential.headers,
                ),
        ) as response:
            if response.status != 200:
                body = await response.read()

                raise RuntimeError(f"HTTP {response.status}: {body}")

            buffer = bytearray()

            async for chunk in response.content.iter_any():
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

            grpc_status = response.headers.get("grpc-status", "0")
            if grpc_status != "0":
                raise RuntimeError(
                    f"gRPC {grpc_status}: {response.headers.get('grpc-message', '?')}"
                )

    async def ask(
        self,
        request: ChatRequest,
        skip_thinking: bool = False,
        chunks_white_list: Optional[Tuple[Type[ResponseChunk], ...]] = None
    ) -> AskResponse:
        tokens = []
        result = AskResponse(text="")

        async for chunk in self.ask_stream(
            request=request,
            skip_thinking=skip_thinking,
            chunks_white_list=chunks_white_list
        ):
            if isinstance(chunk, TokenChunk) and chunk.is_final and chunk.token:
                tokens.append(chunk.token)

            elif isinstance(chunk, ModelResponseChunk):
                result.model_response = chunk.model_response

            elif isinstance(chunk, FinalMetadataChunk):
                result.final_metadata = chunk.final_metadata

            elif isinstance(chunk, SurveyChunk):
                result.survey = chunk.survey

            elif isinstance(chunk, ConversationChunk):
                result.conversation = chunk.conversation

            elif isinstance(chunk, TitleChunk):
                result.title = chunk.new_title

        result.text = "".join(tokens)
        return result
