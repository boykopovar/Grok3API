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
from grok3api.types.exceptions import GrokStreamError
from grok3api.types.request import ChatRequest, AddResponseRequest
from grok3api.utils.constants import GRPC_CHAT, GRPC_ADD_RESPONSE



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

    async def new_ask_stream(
            self,
            request: ChatRequest,
            skip_thinking: bool = True,
            chunks_white_list: Optional[Tuple[Type[ResponseChunk], ...]] = (TokenChunk, ModelResponseChunk, ConversationChunk),
    ) -> AsyncIterator[ResponseChunk]:
        """Stream a request for a new conversation and yield parsed response chunks.

        Sends a fresh chat request to the Grok gRPC chat endpoint and streams parsed
        response chunks as they are received.

        Args:
            request: The chat request for the new conversation.
            skip_thinking: If True, skips TokenChunk objects marked as thinking.
            chunks_white_list: Optional tuple of ResponseChunk types to yield.
                If specified, only chunks matching one of the provided types
                are yielded. If None, all parsed chunks are yielded.

        Returns:
            AsyncIterator[ResponseChunk]: Async iterator yielding parsed response
            chunks. ResponseChunk is a union of all supported chunk models.
        """
        async for chunk in self._stream(GRPC_CHAT, request.encode(), skip_thinking, chunks_white_list):
            yield chunk

    async def add_response_stream(
            self,
            request: AddResponseRequest,
            skip_thinking: bool = True,
            chunks_white_list: Optional[Tuple[Type[ResponseChunk], ...]] = (TokenChunk, ModelResponseChunk),
    ) -> AsyncIterator[ResponseChunk]:
        """Stream a message added to an existing conversation and yield parsed response chunks.

        Sends an add-response request to the Grok gRPC endpoint for an existing
        conversation, decodes streamed frames, optionally skips thinking tokens, and
        filters yielded chunks by type.

        Args:
            request: The add-response request containing the conversation ID and the
                next user message.
            skip_thinking: If True, skips TokenChunk objects marked as thinking.
            chunks_white_list: Optional tuple of ResponseChunk types to yield.
                If specified, only chunks matching one of the provided types are
                yielded. If None, all parsed chunks are yielded.

        Returns:
            AsyncIterator[ResponseChunk]: An async iterator of parsed response chunks.
            ResponseChunk is a union of all supported chunk models
            (for example, TokenChunk, ModelResponseChunk, ConversationChunk).
        """
        async for chunk in self._stream(GRPC_ADD_RESPONSE, request.encode(), skip_thinking, chunks_white_list):
            yield chunk

    async def add_response(
            self,
            request: AddResponseRequest,
            skip_thinking: bool = False,
            chunks_white_list: Optional[Tuple[Type[ResponseChunk], ...]] = None,
            raise_for_stream_errors: bool = False,
    ) -> AskResponse:
        """Send a message to an existing conversation and collect the full response.

        Consumes the response stream produced by `add_response_stream()` and aggregates
        all received chunks into a single AskResponse object.

        Args:
            request: The add-response request containing the conversation ID and the
                next user message.
            skip_thinking: If True, excludes thinking tokens from the collected text.
            chunks_white_list: Optional tuple of ResponseChunk types to collect.
                If specified, only matching chunk types are processed. If None,
                all parsed chunks are processed.
            raise_for_stream_errors: If True, raises GrokStreamError when the final
                model response contains stream errors.

        Returns:
            AskResponse: Aggregated response containing collected text, model response,
            conversation metadata, final metadata, and other parsed stream data.
        """
        return await _collect(
            self.add_response_stream(request, skip_thinking, chunks_white_list),
            raise_for_stream_errors,
        )


    async def new_ask(
            self,
            request: ChatRequest,
            skip_thinking: bool = False,
            chunks_white_list: Optional[Tuple[Type[ResponseChunk], ...]] = None,
            raise_for_stream_errors: bool = False,
    ) -> AskResponse:
        """Send a new conversation request and collect the full response.

        Consumes the response stream produced by `new_ask_stream()` and aggregates
        all received chunks into a single AskResponse object.

        Args:
            request: The chat request for the new conversation.
            skip_thinking: If True, excludes thinking tokens from the collected text.
            chunks_white_list: Optional tuple of ResponseChunk types to collect.
                If specified, only matching chunk types are processed. If None,
                all parsed chunks are processed.
            raise_for_stream_errors: If True, raises GrokStreamError when the final
                model response contains stream errors.

        Returns:
            AskResponse: Aggregated response containing collected text, model response,
            conversation metadata, final metadata, and other parsed stream data.
        """
        return await _collect(
            self.new_ask_stream(request, skip_thinking, chunks_white_list),
            raise_for_stream_errors,
        )


async def _collect(
        stream: AsyncIterator[ResponseChunk],
        raise_for_stream_errors: bool,
) -> AskResponse:
    tokens = []
    result = AskResponse(text="")

    async for chunk in stream:
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
    if raise_for_stream_errors:
        stream_errors = result.model_response.stream_errors
        if stream_errors:
            raise GrokStreamError(stream_errors[0])

    return result
