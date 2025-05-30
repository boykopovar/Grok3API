# Описание объекта `GrokResponse`

## 🚀 Обзор
Объект `GrokResponse` возвращается методом `create` и содержит полную информацию о ответе от API Grok. Этот объект предоставляет как сам ответ модели (текст, изображения, вложения), так и метаданные, связанные с процессом генерации, включая состояние ответа, идентификаторы и дополнительные параметры.

---

### 🎯 **Что возвращает метод create**
Метод `create` возвращает объект `GrokResponse`, который служит основным контейнером для всех данных, полученных от API Grok в ответ на запрос пользователя. Он объединяет текст ответа, сгенерированные изображения, вложения и информацию о состоянии обработки запроса.

---

### 📋 **Структура объекта GrokResponse**

Объект `GrokResponse` включает следующие поля:

| Поле                     | Тип                         | Описание                                                                                 |
|--------------------------|-----------------------------|------------------------------------------------------------------------------------------|
| `modelResponse`          | `ModelResponse`             | Вложенный объект с основным ответом модели (текст, изображения, вложения).               |
| `isThinking`             | `bool`                      | Указывает, продолжает ли модель обработку ответа (`True` — в процессе).                  |
| `isSoftStop`             | `bool`                      | Указывает, был ли ответ остановлен по критерию (например, длина).                        |
| `responseId`             | `str`                       | Уникальный идентификатор ответа.                                                         |
| `conversationId`         | `Optional[str]`             | Идентификатор чата, к которому относится данный ответ.                                   |
| `title`                  | `Optional[str]`             | Заголовок чата, если был сгенерирован или обновлён (иначе `None`).                       |
| `conversationCreateTime` | `Optional[str]`             | Время создания чата (в формате строки ISO 8601) или `None`, если неизвестно.             |
| `conversationModifyTime` | `Optional[str]`             | Время последнего изменения чата (в формате строки ISO 8601) или `None`, если неизвестно. |
| `temporary`              | `Optional[bool]`            | Признак временного чата (`True` — временный, `False` — постоянный, `None` — неизвестно). |
| `error`                  | `Optional[str]`             | Сообщение об ошибке. `None` — если ошибка не произошла.                                  |
| `error_code`             | `Optional[Union[int, str]]` | Код ошибки. `None` — если ошибка не произошла. `Unknown` — если ошибка без кода.         |


---

### 📜 **Подробное описание полей**

- **`modelResponse`**  
  **Тип:** `ModelResponse`  
  Основной вложенный объект, содержащий ответ модели. Включает текст (`message`), сгенерированные изображения (`generatedImages`), вложения и дополнительные метаданные. Для доступа к тексту используйте `modelResponse.message`.

- **`isThinking`**  
  **Тип:** `bool`  
  Показывает, находится ли модель в процессе генерации ответа. Если `False`, ответ полностью готов.

- **`isSoftStop`**  
  **Тип:** `bool`  
  Указывает, был ли процесс генерации прерван по критерию, например, из-за достижения максимальной длины текста.

- **`responseId`**  
  **Тип:** `str`  
  Уникальный идентификатор ответа, который можно использовать для отслеживания или связи с запросом.

- **`newTitle`**  
  **Тип:** `Optional[str]`  
  Опциональный заголовок, который может быть сгенерирован или обновлён в процессе обработки. Если заголовок не изменялся, значение равно `None`.

---

### 🌟 **Пример использования**

```python
from grok3api.client import GrokClient


def main():
    cookies = "YOUR_COOKIES_FROM_BROWSER"
    
    # Создаём клиент
    client = GrokClient(cookies=cookies)

    # Отправляем запрос
    response = client.ask(message="Привет, Grok!")

    # Выводим текст ответа
    print(response.modelResponse.message)  # "Здравствуйте! Чем могу помочь?"

    # Проверяем, завершён ли ответ
    print(response.isThinking)  # False (ответ готов)

    # Выводим идентификатор ответа
    print(response.responseId)  # "abc123XYZ"

    # Проверяем новый заголовок
    print(response.newTitle)  # None или новый заголовок


if __name__ == '__main__':
    main()
```

---

### 🔗 **Связанные объекты**

- **`ModelResponse`**  
  Вложенный объект внутри `GrokResponse`, содержащий текст ответа, вложения (например, изображения или файлы) и метаданные. Подробности описаны ниже.

- **`GeneratedImage`**  
  Объект для работы со сгенерированными изображениями, доступный через `modelResponse.generatedImages`. Используется для загрузки и сохранения изображений.

---

### 📌 **Примечания**

- **`GrokResponse` как контейнер**  
  Этот объект объединяет всю информацию об ответе API и предоставляет удобный доступ к данным через свои поля.

- **Доступ к тексту ответа**  
  Используйте `response.modelResponse.message`, чтобы получить текст ответа.

- **Работа с изображениями**  
  Если в ответе есть изображения, они доступны через `response.modelResponse.generatedImages`. Каждое изображение — объект `GeneratedImage` с методами для загрузки и сохранения.

---

## 📋 **Дополнительно: Структура объекта ModelResponse**

`ModelResponse` — ключевая часть `GrokResponse`, содержащая детализированный ответ модели. Вот обновлённая структура его полей:

| Поле                      | Тип                    | Описание                                                                   |
|---------------------------|------------------------|----------------------------------------------------------------------------|
| `responseId`              | `str`                  | Уникальный идентификатор ответа.                                           |
| `message`                 | `str`                  | Текст ответа модели.                                                       |
| `sender`                  | `str`                  | Отправитель сообщения (обычно "ASSISTANT").                                |
| `createTime`              | `str`                  | Время создания ответа в формате ISO.                                       |
| `parentResponseId`        | `str`                  | ID сообщения, на которое отвечает данный ответ.                            |
| `manual`                  | `bool`                 | Указывает, создан ли ответ вручную (`False` — сгенерирован моделью).       |
| `partial`                 | `bool`                 | Указывает, является ли ответ неполным (`True` — ещё генерируется).         |
| `shared`                  | `bool`                 | Указывает, разделён ли ответ с другими (`True` — да, `False` — приватный). |
| `query`                   | `str`                  | Оригинальный запрос пользователя.                                          |
| `queryType`               | `str`                  | Тип запроса (для аналитики).                                               |
| `webSearchResults`        | `List[Any]`            | Результаты веб-поиска, использованные моделью.                             |
| `xpostIds`                | `List[Any]`            | IDs X-постов, на которые ссылалась модель.                                 |
| `xposts`                  | `List[Any]`            | X-посты, на которые ссылалась модель.                                      |
| `generatedImages`         | `List[GeneratedImage]` | Список сгенерированных изображений.                                        |
| `imageAttachments`        | `List[Any]`            | Список вложений изображений.                                               |
| `fileAttachments`         | `List[Any]`            | Список вложений файлов.                                                    |
| `cardAttachmentsJson`     | `List[Any]`            | JSON-данные для вложений типа "карточка".                                  |
| `fileUris`                | `List[Any]`            | URIs прикреплённых файлов.                                                 |
| `fileAttachmentsMetadata` | `List[Any]`            | Метаданные вложений файлов.                                                |
| `isControl`               | `bool`                 | Указывает, является ли ответ системным (например, сообщение об ошибке).    |
| `steps`                   | `List[Any]`            | Шаги или процесс рассуждений модели для генерации ответа.                  |
| `mediaTypes`              | `List[Any]`            | Типы медиа в ответе (например, "image", "file").                           |

> 💡 Не все поля используются в каждом запросе. Например, `webSearchResults` или `steps` заполняются только при определённых условиях.

---

## 📋 **Дополнительно: Структура объекта GeneratedImage**

Объект `GeneratedImage` используется для работы с изображениями, доступными через `modelResponse.generatedImages`:

| Поле        | Тип   | Описание                                                          |
|-------------|-------|-------------------------------------------------------------------|
| `cookies`   | `str` | Cookies для доступа к изображению (на случай перезапуска Chrome). |
| `url`       | `str` | Неполный URL изображения (`anon-users/...-generated_image.jpg`).  |
| `_base_url` | `str` | Базовый URL (по умолчанию "https://assets.grok.com").             |

### Методы `GeneratedImage`
- **`download() -> Optional[BytesIO]`**  
  Загружает изображение и возвращает его как объект `BytesIO`.

- **`save_to(path: str) -> bool`**  
  Сохраняет изображение в файл по указанному пути.


#### Пример работы с изображением:

```python
from grok3api.client import GrokClient


def main():
    cookies = "YOUR_COOKIES_FROM_BROWSER"
    
    # Создаём клиент
    client = GrokClient(cookies=cookies)

    # Отправляем запрос для создания изображения
    response = client.ask(message="Создай изображение корабля")

    # Проверяем, есть ли сгенерированные изображения, и сохраняем первое
    if response.modelResponse.generatedImages:
        image = response.modelResponse.generatedImages[0]
        image.save_to("ship.jpg")  # Сохраняет изображение как ship.jpg
        print("Изображение корабля сохранено как ship.jpg")
    else:
        print("Изображения не были сгенерированы.")


if __name__ == '__main__':
    main()
```

---

### 🛠️ **Советы по использованию**

- **Получение текста:** Используйте `response.modelResponse.message` для быстрого доступа к тексту.
- **Проверка статуса:** Поле `isThinking` показывает, завершён ли ответ (скоро будет добавлена возможность получения ответа по частям).
- **Работа с изображениями:** Используйте методы `download()` и `save_to()` для загрузки и сохранения картинок.
- **Эксперименты:** Пробуйте разные параметры в методе `create`, чтобы раскрыть дополнительные возможности.