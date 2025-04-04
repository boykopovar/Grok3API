🚀 Библиотека Python для взаимодействия с API Grok 3 с необходимостью ввода cookies.
## [➡ English ReadMe](../../README.md)

# 🤖 Grok3API: Клиент для работы с Grok

**Grok3API** — это мощный и удобный неофициальный инструмент для взаимодействия с моделями Grok (включая Grok3), который позволяет отправлять запросы, получать текстовые ответы и, что особенно круто, **сгенерированные изображения**. 🎨✨ Проект разработан с упором на простоту использования и автоматизацию, чтобы вы могли сосредоточиться на творчестве, а не на технических деталях.

---

## 🌟 Возможности

- 🖼️ **Удобное получение сгенерированных изображений** с методом `save_to`, который позволяет сохранить их в один клик.
- 🔧 **Гибкая настройка запросов**: выбор модели, управление генерацией изображений, добавление вложений и многое другое.
- 📦 **Поддержка вложений**: отправляйте файлы и изображения вместе с запросами.
- 🤖 **[Пример Telegram бота](../../tests/SimpleTgBot/SimpleTgBot.py) (`grok3api` + `aiogram`)**, с возможностью создавать текстовые ответы и изображения.
---

## 📦 Установка

Чтобы начать использовать GrokClient, установите необходимые зависимости. Всё просто:

```bash
pip install grok3api
```

> ⚠️ **Важно**: Убедитесь, что у вас установлен **Google Chrome**, так как `undetected_chromedriver` работает именно с ним.

После установки вы готовы к запуску! 🎉

---

## 🚀 Использование


### Быстрый старт  

Вот полный пример, как отправить запрос и сохранить сгенерированное изображение:

```python
from grok3api.client import GrokClient


def main():
  
    cookies = "YOUR_COOKIES_FROM_BROWSER"
    
    # Создаём клиент
    client = GrokClient(cookies=cookies)

    # Создаём запрос
    message = "Создай изображение корабля"

    # Отправляем запрос
    result = client.ask(message)
    print("Ответ Grok:", result.modelResponse.message)

    # Сохраняем первое изображение, если оно есть
    if result.modelResponse.generatedImages:
        result.modelResponse.generatedImages[0].save_to("ship.jpg")
        print("Изображение сохранено как ship.jpg! 🚀")


if __name__ == '__main__':
    main()
```

Этот код:  
1. **Создаёт клиента**.  
2. **Отправляет запрос** на генерацию изображения.  
3. **Сохраняет изображение** в файл `ship.jpg`.  

📌 **Что мы увидим?**  
Grok сгенерирует изображение **корабля**, например, вот такое:  

<img src="../../assets/ship.jpg" alt="Пример корабля" width="500">



---

## 🔧 Параметры запроса

Метод `GrokClient.ask` принимает множество параметров для настройки вашего запроса. Вот пример с настройками:

```python
from grok3api.client import GrokClient


def main():
    cookies = "YOUR_COOKIES_FROM_BROWSER"
    
    # Создаём клиент
    client = GrokClient(cookies=cookies)

    # Отправляем запрос с настройками
    result = client.ask(
        message="Нарисуй кота",
        modelName="grok-3",  # По умолчанию и так grok-3
        imageGenerationCount=2,  # Хочу 2 изображения кота!
    )
    print(f"Ответ Grok3: {result.modelResponse.message}")

    # Сохраняем все изображения
    for i, img in enumerate(result.modelResponse.generatedImages):
        img.save_to(f"cat_{i}.jpg")
        print(f"Сохранено: cat_{i}.jpg 🐾")


if __name__ == '__main__':
    main()
```

### [💼️ Описания класса `GrokClient`](ClientDoc.md)
### [✈️ Описания метода `ask`](askDoc)
### [📋 Описание класса `History`](HistoryDoc.md)
### [📬 Описание класса `GrokResponse`](GrokResponse.md)
### [🐧 Особенности работы с `Linux`](LinuxDoc.md)

---

## 🖼️ Удобное получение изображений

Одна из главных фишек GrokClient — это **супер-удобная работа со сгенерированными изображениями**. Вот полный пример:

```python
from grok3api.client import GrokClient


def main():
    cookies = "YOUR_COOKIES_FROM_BROWSER"
    
    # Создаём клиент
    client = GrokClient(cookies=cookies)

    # Отправляем запрос
    result = client.ask("Нарисуй закат над морем")

    # Сохраняем все изображения
    for i, image in enumerate(result.modelResponse.generatedImages):
        image.save_to(f"sunset_{i}.jpg")
        print(f"Сохранено: sunset_{i}.jpg 🌅")


if __name__ == '__main__':
    main()
```


---


## 📋 Обработка ответов

Метод `ask` возвращает объект `GrokResponse`. Вот пример работы с ним:

```python
from grok3api.client import GrokClient


def main():
    cookies = "YOUR_COOKIES_FROM_BROWSER"
    
    # Создаём клиент
    client = GrokClient(cookies=cookies)

    # Отправляем запрос
    result = client.ask("Опиши и нарисуй лес")

    # Обрабатываем ответ
    print(f"Текст: {result.modelResponse.message}")
    result.modelResponse.generatedImages[0].save_to("forest.jpg")


if __name__ == '__main__':
    main()
```

Поля объекта `GrokResponse`:
- **`modelResponse`**: Основной ответ модели.
  - `message` (str): Текстовый ответ.
  - `generatedImages` (List[GeneratedImage]): Список изображений.
- **`isThinking`**: Думала ли модель (bool).
- **`isSoftStop`**: Мягкая остановка (bool).
- **`responseId`**: ID ответа (str).
- **`newTitle`**: Новый заголовок чата, если есть (Optional[str]).

---


Если что-то неясно, пишите в issues — разберёмся вместе! 🌟

## 📄 Лицензия

Проект распространяется под лицензией **MIT**. Подробности — в файле [LICENSE](../../LICENSE).





## Дисклеймер
### Введение
Grok3API — это сторонний клиент для взаимодействия с Grok.

Grok3API не имеет связи с xAI или разработчиками Grok. Это независимый проект, созданный третьей стороной, и он не поддерживается, не спонсируется и не одобряется xAI. Любые проблемы, связанные с API Grok, должны решаться напрямую с xAI.

### Ответственность и гарантии
Программное обеспечение предоставляется "как есть", без каких-либо гарантий, включая пригодность для конкретных целей или отсутствие ошибок. Создатель Grok3API не несет ответственности за любые убытки или ущерб, возникшие в результате использования клиента. Вы используете его на свой риск.

### Соответствие законам
Вы несете ответственность за то, чтобы ваше использование Grok3API соответствовало всем применимым законам и регулированиям. Создатель не поощряет незаконное использование.
Grok3API требует полного соблюдения правил xAI API.