import asyncio
from typing import Union, AsyncIterator

from grok3api.client import GrokClient
from grok3api.types import (
    ResponseChunk,
    TokenChunk,
    ConversationChunk,
    ModelResponseChunk,
)
from grok3api.types.request import ChatRequest, AddResponseRequest
from grok3api.types.exceptions import GrokUnderHeavyUsageError


async def stream_with_retry(
        client: GrokClient,
        request: Union[ChatRequest, AddResponseRequest]
) -> AsyncIterator[ResponseChunk]:
    while True:
        try:
            if isinstance(request, ChatRequest):
                async for chunk in client.new_ask_stream(request, skip_thinking=True):
                    yield chunk
            else:
                async for chunk in client.add_response_stream(request, skip_thinking=True):
                    yield chunk

            return

        except GrokUnderHeavyUsageError:
            print("Heavy usage, retrying...")


async def main() -> None:
    async with GrokClient() as client:
        conversation_id = None
        parent_response_id = None

        while True:
            message = input("\nYou: ")

            if conversation_id is None:
                request = ChatRequest(
                    message=message,
                    temporary=False,
                )
            else:
                request = AddResponseRequest(
                    message=message,
                    conversation_id=conversation_id,
                    parent_response_id=parent_response_id,
                )

            started = False

            async for chunk in stream_with_retry(client, request):
                if isinstance(chunk, TokenChunk):
                    if chunk.token and chunk.is_final:
                        if not started:
                            started = True
                            print("\nGrok: ", end="", flush=True)

                        print(chunk.token, end="", flush=True)

                elif isinstance(chunk, ConversationChunk):
                    conversation_id = chunk.conversation.conversation_id

                elif isinstance(chunk, ModelResponseChunk):
                    parent_response_id = chunk.model_response.response_id


if __name__ == "__main__":
    asyncio.run(main())