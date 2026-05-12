import asyncio

from grok3api.client import GrokClient
from grok3api.types.request import ChatRequest, DeviceEnvInfo
from grok3api.types import (
    ConversationChunk,
    FinalMetadataChunk,
    ModelResponseChunk,
    TitleChunk,
    TokenChunk,
)


async def main() -> None:
    async with GrokClient() as client:
        request = ChatRequest(
            message="даров",
            temporary=False
        )

        print("=== ask_stream ===")

        async for chunk in client.ask_stream(request):
            if (
                isinstance(chunk, TokenChunk)
                and chunk.message_tag == "final"
            ):
                print(chunk.token, end="", flush=True)

            elif isinstance(chunk, ConversationChunk):
                print(
                    "\n[conversation_id={}]".format(
                        chunk.conversation.conversation_id,
                    ),
                )

            elif isinstance(chunk, TitleChunk):
                print(
                    "[title={}]".format(
                        chunk.new_title,
                    ),
                )

            elif isinstance(chunk, FinalMetadataChunk):
                suggestions = [
                    suggestion.label
                    for suggestion in (
                        chunk.final_metadata.follow_up_suggestions
                    )
                ]

                print(
                    "[follow_ups={}]".format(
                        suggestions,
                    ),
                )

            elif isinstance(chunk, ModelResponseChunk):
                model_response = chunk.model_response

                print(
                    "[model={} thinking={}..{}]".format(
                        model_response.model,
                        model_response.thinking_start_time,
                        model_response.thinking_end_time,
                    ),
                )

        print()

        print("\n=== ask ===")

        result = await client.ask(request)

        print("text: {!r}".format(result.text))

        if result.model_response is not None:
            print(
                "model: {}".format(
                    result.model_response.model,
                ),
            )

            print(
                "steps: {}".format(
                    [
                        (step.tags, step.text)
                        for step in result.model_response.steps
                    ],
                ),
            )

        if result.final_metadata is not None:
            print(
                "follow_ups: {}".format(
                    [
                        suggestion.label
                        for suggestion in (
                            result.final_metadata.follow_up_suggestions
                        )
                    ],
                ),
            )

        if result.conversation is not None:
            print(
                "conversation_id: {}".format(
                    result.conversation.conversation_id,
                ),
            )

        if result.title is not None:
            print(
                "title: {}".format(
                    result.title,
                ),
            )


if __name__ == "__main__":
    asyncio.run(main())