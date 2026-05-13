# Grok3API

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)
![Reverse engineered](https://img.shields.io/badge/Reverse%20engineered%20with-🔬-red)

![Stars](https://img.shields.io/github/stars/boykopovar/Grok3API?style=social)
![Forks](https://img.shields.io/github/forks/boykopovar/Grok3API?style=social)
![Issues](https://img.shields.io/github/issues/boykopovar/Grok3API?style=social)

Библиотека для асинхронной работы с Grok через мобильный gRPC-канал: отправка сообщений, потоковый вывод ответа, парсинг protobuf-чанков и получение структурированных данных API.


## Особенности

- асинхронный клиент
- streaming-ответ через `new_ask_stream()`
- обычный запрос через `new_ask()`
- protobuf/gRPC framing
- типизированные Pydantic-модели
- потоковый парсинг чанков
- обработка REST/gRPC/stream ошибок
- поддержка metadata/tool responses/search results


## Установка

```bash
pip install git+ssh://git@github.com/boykopovar/Grok3API.git -U
```

## Зависимости

* Python 3.8+
* aiohttp
* coincurve

## Streaming пример

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

## Обычный запрос

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

## Продолжение начатого диалога

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



## Pydantic-модели

Все модели полностью соответствуют реальным protobuf/gRPC ответам API.

В библиотеке отсутствуют:

- упрощённые структуры
- искусственные abstraction layers
- нормализация полей
- переименование payload-данных
- скрытие оригинальных значений API


## Что поддерживается

### Response chunks

- `TokenChunk`
- `ModelResponseChunk`
- `FinalMetadataChunk`
- `SurveyChunk`
- `ConversationChunk`
- `TitleChunk`

### Response models

- `AskResponse`
- `ModelResponse`
- `FinalMetadata`
- `Conversation`
- `Survey`
- `ResponseStep`
- `ToolUsageResult`
- `WebSearchResult`
- `XPost`
- `RagResult`
- `CollectionSearchResultItem`
- `ConnectorSearchResultItem`
- `StreamError`

### Tool responses

- web search
- X/Twitter search
- RAG results
- connector search
- collection search
- memory updates
- code execution
- image generation
- video generation
- audio generation


## Обработка ошибок

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

## Как работает клиент

1. protobuf request сериализуется в binary payload
2. payload упаковывается в gRPC frame
3. запрос отправляется в mobile gRPC endpoint
4. клиент читает streaming response
5. protobuf chunks декодируются в Pydantic-модели

## Disclaimer

Проект не связан с xAI и не является официальным SDK.

Это независимая реализация мобильного Grok API, полученная в результате реверс-инжиниринга.
