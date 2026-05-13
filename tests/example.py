import asyncio
from typing import Union

from grok3api.client import GrokClient
from grok3api.types import AskResponse
from grok3api.types.request import ChatRequest, AddResponseRequest
from grok3api.types.exceptions import GrokUnderHeavyUsageError


async def stream_with_retry(
        client: GrokClient,
        request: Union[ChatRequest, AddResponseRequest]
) -> AskResponse:
    while True:
        try:
            if isinstance(request, ChatRequest):
                return await client.ask(request, skip_thinking=True)
            return await client.add_response(request, skip_thinking=True)
        except GrokUnderHeavyUsageError:
            print("Heavy usage, retrying...")


async def main() -> None:
    async with GrokClient() as client:
        conversation_id = None
        parent_response_id = None

        while True:
            message = input("\nYou: ")

            if conversation_id is None:
                request = ChatRequest(message=message, temporary=False)
            else:
                request = AddResponseRequest(
                    message=message,
                    conversation_id=conversation_id,
                    parent_response_id=parent_response_id,
                )

            result = await stream_with_retry(client, request)

            if conversation_id is None:
                conversation_id = result.conversation.conversation_id

            parent_response_id = result.model_response.response_id

            print(f"\nGrok: {result.text}")


if __name__ == "__main__":
    asyncio.run(main())