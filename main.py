import asyncio

from grok3api.client import GrokClient
from grok3api.types.request import ChatRequest
from grok3api.types import TokenChunk


async def ask_grok(client: GrokClient, request: ChatRequest):
    async for chunk in client.ask_stream(request):  # type: TokenChunk
        print(chunk.token, end="", flush=True)


async def main() -> None:
    async with GrokClient() as client:
        request = ChatRequest(
            message="Даров как сам? Как день прошел?",
            temporary=False
        )
        await asyncio.gather(
            *[ask_grok(client, request) for _ in range(5)],
            return_exceptions=True
        )




if __name__ == "__main__":
    asyncio.run(main())