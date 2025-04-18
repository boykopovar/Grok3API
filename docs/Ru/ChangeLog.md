## 📦 Changelog

---

### 🆕 v0.0.1b11

#### ✨ Новое:
- 🖼️ **Поддержка отправки изображений в Grok**  
  Теперь стало намного проще отправлять изображения на сервер Grok!

```python
from grok3api.client import GrokClient


def main():
    client = GrokClient()
    result = client.ask(
        message="Что на картинке?",
        images="C:\\photo1_to_grok.jpg"
    )
    print(f"Ответ Grok3: {result.modelResponse.message}")

if __name__ == '__main__':
    main()
```

Подробное описание метода отправки доступно [здесь](askDoc.md).

- 🤖 **Продолжается работа над OpenAI-совместимостью**  
  - ✅ Теперь поддерживаются **любые `api_key`** для работы с сервером.
  - ⚙️ Добавлена возможность настройки сервера (через аргументы командной строки и переменные окружения). Подробная инструкция по запуску доступна в [🌐 Запуск OpenAI-совместимого сервера](OpenAI_Server.md).

> ⚠️ **Сервер всё ещё находится на ранней стадии, некоторые функции могут быть нестабильными.**

---

### 🆕 v0.0.1b10

#### ✨ Новое:
- 🔐 **Автоматическое получение cookies**  
  Теперь больше **не обязательно указывать cookies вручную** — клиент сам их получит при необходимости.  
  ➕ Однако, вы **всё ещё можете указать свои cookies**, если хотите использовать свой аккаунт (например, для генерации с кастомными настройками или доступом к платным возможностям).

- 🤖 **Начало работы над OpenAI-совместимостью ([**server.py**](../../grok3api/server.py), [**Demo**](../../tests/openai_test.py))**  
  Реализован первый черновик сервера, совместимого с API OpenAI. Пока **работает "как-то"**, но:
  > ⚠️ **Находится на ранней стадии и не отлажен. Используйте на свой страх и риск!**

---