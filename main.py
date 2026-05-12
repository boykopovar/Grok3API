import asyncio

from grok3api.client import GrokClient
from grok3api.types.exceptions import GrokUnderHeavyUsageError
from grok3api.types.request import ChatRequest


async def ask_grok(client: GrokClient, request: ChatRequest):
    response = await client.ask(
        request,
        raise_for_stream_errors=True,
    )
    print(response)


async def main() -> None:
    async with GrokClient() as client:
        request = ChatRequest(
            message="Что я только что спросил?",
            temporary=False
        )
        await asyncio.gather(
            *[ask_grok(client, request) for _ in range(1)],
            return_exceptions=False
        )


if __name__ == "__main__":
    asyncio.run(main())