# Grok3API

<p align="left">
  <img src="docs/assets/icon.svg" width="90">
</p>

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python\&logoColor=white)
![Reverse engineered](https://img.shields.io/badge/Reverse%20engineered%20with-🔬-red)

![Stars](https://img.shields.io/github/stars/boykopovar/Grok3API?style=social)
![Forks](https://img.shields.io/github/forks/boykopovar/Grok3API?style=social)
![Issues](https://img.shields.io/github/issues/boykopovar/Grok3API?style=social)

An asynchronous library for interacting with Grok via the mobile gRPC channel: sending messages, streaming responses, parsing protobuf chunks, and retrieving structured API data.

---

## [➡ Ru README](docs/Ru/RuReadMe.md)


## Features

* asynchronous client
* streaming responses via `new_ask_stream()`
* regular requests via `new_ask()`
* protobuf/gRPC framing
* typed Pydantic models
* streaming chunk parsing
* REST/gRPC/stream error handling
* support for metadata/tool responses/search results

## Installation

```bash
pip install git+ssh://git@github.com/boykopovar/Grok3API.git -U
```

## Requirements

* Python 3.8+
* aiohttp
* coincurve

## Streaming Example

```python
import asyncio

from grok3api.client import GrokClient
from grok3api.types.request import ChatRequest
from grok3api.types import TokenChunk


async def main():
    async with GrokClient() as client:
        while True:
            print("\nGrok: ", end="")

            async for chunk in client.new_ask_stream(
                request=ChatRequest(
                    message=input("\nYou: "),
                    temporary=False
                ),
                chunks_white_list=(TokenChunk,)
            ):
                print(chunk.token, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
```

## Standard Request

```python
import asyncio

from grok3api.client import GrokClient
from grok3api.types.request import ChatRequest


async def main():
    async with GrokClient() as client:
        response = await client.new_ask(
            ChatRequest(
                message="Hello",
                temporary=False
            )
        )

        print(response.text)
        print(response.model_response)


if __name__ == "__main__":
    asyncio.run(main())
```

## Continue started conversation

```python
import asyncio

from grok3api.client import GrokClient
from grok3api.types.request import ChatRequest, AddResponseRequest


async def main():
    async with GrokClient() as client:
        first = await client.new_ask(
            ChatRequest(
                message="Hello",
                temporary=False
            )
        )

        second = await client.add_response(
            AddResponseRequest(
                conversation_id=first.conversation.conversation_id,
                message="How are you?"
            )
        )

        print(second.text)


if __name__ == "__main__":
    asyncio.run(main())
```

## Pydantic Models

All models fully match the actual protobuf/gRPC API responses.

The library does not include:

* simplified structures
* artificial abstraction layers
* field normalization
* payload field renaming
* hiding original API values

## Supported

### Response Chunks

* `TokenChunk`
* `ModelResponseChunk`
* `FinalMetadataChunk`
* `SurveyChunk`
* `ConversationChunk`
* `TitleChunk`

### Response Models

* `AskResponse`
* `ModelResponse`
* `FinalMetadata`
* `Conversation`
* `Survey`
* `ResponseStep`
* `ToolUsageResult`
* `WebSearchResult`
* `XPost`
* `RagResult`
* `CollectionSearchResultItem`
* `ConnectorSearchResultItem`
* `StreamError`

### Tool Responses

* web search
* X/Twitter search
* RAG results
* connector search
* collection search
* memory updates
* code execution
* image generation
* video generation
* audio generation

## Error Handling

```python
from grok3api.types.exceptions import (
    GrokApiError,
    GrokRestError,
    GrokGrpcError,
    GrokRateLimitError,
    GrokUnderHeavyUsageError,
    GrokStreamError,
    GrokUnavailableRegionError,
    GrokTooManyRequestsError
)
```

## How the Client Works

1. the protobuf request is serialized into a binary payload
2. the payload is wrapped into a gRPC frame
3. the request is sent to the mobile gRPC endpoint
4. the client reads the streaming response
5. protobuf chunks are decoded into Pydantic models

## Disclaimer

This project is not affiliated with xAI and is not an official SDK.

This is an independent implementation of the mobile Grok API obtained through reverse engineering.
