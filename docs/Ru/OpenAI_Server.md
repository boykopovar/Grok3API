# 🧠 Grok3API OpenAI-Compatible Server

> 🤖 **Ранняя стадия разработки сервера**

Реализован первый черновик сервера, совместимого с OpenAI API (`/v1/chat/completions`).

> ⚠️ **Находится на ранней стадии и не отлажен. Используйте на свой страх и риск!**

---

### ⚙️ Запуск сервера

> Убедитесь, что у вас установлен `fastapi`, `uvicorn`, `pydantic`, и сам `grok3api`.

```bash
# В корне проекта:
python -m grok3api.server
```

```bash
# Или можете настроить адрес и порт
python -m grok3api.server --host 127.0.0.1 --port 9000
```

🎉 Сервер запустится на `http://127.0.0.1:9000`.

> Используется `uvicorn` под капотом. Убедитесь, что структура проекта позволяет модульный запуск (через `-m`).

---

## 🔁 Эндпоинт: `/v1/chat/completions`

Совместим с OpenAI форматом запросов:

### 📥 Пример запроса:

```python
from openai import OpenAI
from openai import OpenAIError

# Создание клиента с заданным URL и ключом
client = OpenAI(
    base_url="http://localhost:9000/v1",
    api_key="dummy"
)

try:
    # Отправка запроса на сервер
    response = client.chat.completions.create(
        model="grok-3",
        messages=[{"role": "user", "content": "Что такое Python?"}]
    )

    # Вывод ответа от сервера
    print("Ответ сервера:")
    print(f"Модель: {response.model}")
    print(f"Сообщение: {response.choices[0].message.content}")
    print(f"Причина завершения: {response.choices[0].finish_reason}")
    print(f"Использование: {response.usage}")

except OpenAIError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")

```

> `stream` не поддерживается, будет возвращён `400 Bad Request`.


### 📤 Вывод:

```
Ответ сервера:
Модель: grok-3
Сообщение: Python — это высокоуровневый, интерпретируемый язык программирования с простым и читаемым синтаксисом. Он поддерживает разные парадигмы программирования (объектно-ориентированное, функциональное, процедурное) и широко используется для веб-разработки, анализа данных, автоматизации задач, машинного обучения и других целей. Python популярен благодаря своей универсальности, обширной стандартной библиотеке и большому сообществу разработчиков.
Причина завершения: stop
Использование: CompletionUsage(completion_tokens=46, prompt_tokens=3, total_tokens=49, completion_tokens_details=None, prompt_tokens_details=None)
```

---


## 🧵 Эндпоинт: `/v1/string` (GET)

Простой текстовый GET-запрос. Принимает строку как query-параметр и возвращает ответ от Grok без JSON-обёртки.

### 📥 Пример запроса:

Откройте в браузере или используйте `curl`:

```bash
curl http://localhost:9000/v1/string?q=Привет
```

### 📤 Пример ответа:

```
Привет! Чем могу помочь?
```

### 🐍 Пример из Python:

```python
import requests

response = requests.get("http://localhost:9000/v1/string", params={"q": "Расскажи анекдот"})
print(response.text)  # Просто текст, без JSON
```

---


## 🧵 Эндпоинт: `/v1/string` (POST)

Простой текстовый POST-запрос. Принимает строку в теле запроса и возвращает ответ от Grok без JSON-обёртки.

### 📥 Пример запроса:

Используйте `curl` или другой инструмент:

```bash
curl -X POST http://localhost:9000/v1/string -d "Привет"
```

### 📤 Пример ответа:

```
Привет! Чем могу помочь?
```

### 🐍 Пример из Python:

```python
import requests

response = requests.post("http://localhost:9000/v1/string", data="Расскажи анекдот")
print(response.text)  # Просто текст, без JSON
```


---

## ⚙️ Переменные окружения (опционально)

| Переменная         | Описание                                   | По умолчанию |
|--------------------|--------------------------------------------|--------------|
| `GROK_COOKIES`     | Куки-файл для GrokClient                   | `None`       |
| `GROK_PROXY`       | Прокси (например: `http://localhost:8080`) | `None`       |
| `GROK_TIMEOUT`     | Таймаут запросов Grok (в секундах)         | `120`        |
| `GROK_SERVER_HOST` | IP для запуска сервера                     | `0.0.0.0`    |
| `GROK_SERVER_PORT` | Порт для запуска сервера                   | `8000`       |





---

## 📂 Структура проекта

```
Grok3API/
├── grok3api/
│   ├── server.py          # <--- запуск сервера
│   ├── client.py
│   ├── types/
│   └── ...
├── tests/
│   └── openai_test.py     # <--- тест совместимости
└── README.md
```

---

## ❗ TODO / Known Issues

- [ ] 🔄 Поддержка стриминга (`stream=True`)
- [ ] 🧪 Больше тестов и валидации
- [ ] 🧼 Рефакторинг `message_payload` и логики истории
- [ ] 🧩 Кастомные инструкции, изображения и доп. фичи

---

💬 По вопросам и предложениям — welcome в issues!
```