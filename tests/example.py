import asyncio

from grok3api.client import GrokClient
from grok3api.types.request import ChatRequest



async def main() -> None:
    async with GrokClient() as client:
        while True:
            request = ChatRequest(
                message=input("\nYou: "),
                temporary=False
            )

            print("\nGrok: ", end="")
            async for chunk in client.ask_stream(request):
                print(chunk.token, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())