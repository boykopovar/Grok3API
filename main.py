import asyncio

from grok3api.client import GrokClient
from grok3api.types.exceptions import GrokUnderHeavyUsageError
from grok3api.types.request import ChatRequest
from grok3api.types import TokenChunk


async def main():
    async with GrokClient() as client:
        while True:
            request = ChatRequest(
                message=input("\nYou: "),
                temporary=False
            )
            print("\nGrok: ", end="")

            run = True
            while run:
                try:
                    async for chunk in client.new_ask_stream(
                        request=request,
                        chunks_white_list=(TokenChunk,)
                    ):
                        print(chunk.token, end="", flush=True)
                        run = False
                except GrokUnderHeavyUsageError as e:
                    print(e)


if __name__ == "__main__":
    asyncio.run(main())