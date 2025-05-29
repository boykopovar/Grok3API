🚀 Библиотека Python для взаимодействия с API Grok 3 без необходимости входа в систему или необходимости ввода файлов cookie. Идеально подходит для использования «из коробки».
## [➡ English ReadMe](../../README.md)

# 🤖 Grok3API: Клиент для работы с Grok

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)
![Made with ❤️](https://img.shields.io/badge/Made%20with-%F0%9F%92%9C-red)

![Stars](https://img.shields.io/github/stars/boykopovar/Grok3API?style=social)
![Forks](https://img.shields.io/github/forks/boykopovar/Grok3API?style=social)
![Issues](https://img.shields.io/github/issues/boykopovar/Grok3API?style=social)


**Grok3API** — это мощный и удобный неофициальный инструмент для взаимодействия с моделями Grok (включая Grok3), который позволяет отправлять запросы, получать текстовые ответы и, что особенно круто, **сгенерированные изображения** — всё это с автоматическим управлением cookies! 🎨✨ Проект разработан с упором на простоту использования и автоматизацию, чтобы вы могли сосредоточиться на творчестве, а не на технических деталях.


---

## [📦 Подробный Changelog](ChangeLog.md)

### 🆕 v0.1.0b1

#### ✨ Новое:

* 🛠 **Улучшена обработка код-блоков**
  Добавлена автоматическая трансформация вложенных блоков `<xaiArtifact contentType="text/...">...</xaiArtifact>` в стандартные Markdown-блоки с указанием языка.

* ☑️ Функцию можно отключить, указав параметр `auto_transform_code_blocks=False` при создании `GrokClient`.

---



## 🌟 Возможности

- 🚀 **Автоматическое получение cookies** через браузер с обходом Cloudflare — никаких ручных настроек!
- 🖼️ **Удобное получение сгенерированных изображений** с методом `save_to`, который позволяет сохранить их в один клик.
- 🔧 **Гибкая настройка запросов**: выбор модели, управление генерацией изображений, добавление вложений и многое другое.
- 📦 **Поддержка вложений**: отправляйте файлы и изображения вместе с запросами.
- 🛠️ **Обработка ошибок**: клиент сам решает проблемы с cookies и повторяет запросы, если что-то пошло не так.
- 🤖 **[Пример Telegram бота](../../tests/SimpleTgBot/SimpleTgBot.py) (`grok3api` + `aiogram`)**
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

🍀 Минимальный рабочий пример:

```python
from grok3api.client import GrokClient

grok = GrokClient()
answer = grok.ask("Привет! Как дела?")

print(answer.modelResponse.message)
```

Вот полный пример, как отправить запрос и сохранить сгенерированное изображение:

```python
from grok3api.client import GrokClient

# Создание клиента (cookies будут автоматически получены, если не переданы)
client = GrokClient()

# Создаём запрос
message = "Создай изображение корабля"

# Отправляем запрос
result = client.ask(message=message,
                    images="C:\\Users\\user\\Downloads\\photo1_to_grok.jpg") # Вы можете отправлять картинку Гроку

print("Ответ Grok:", result.modelResponse.message)

# Сохраняем первое изображение, если оно есть
if result.modelResponse.generatedImages:
    result.modelResponse.generatedImages[0].save_to("ship.jpg")
    print("Изображение сохранено как ship.jpg! 🚀")
```

Этот код:  
1. **Создаёт клиента** — автоматически получает cookies, если их нет.
2. **Отправляет запрос** на генерацию изображения.  
3. **Сохраняет изображение** в файл `ship.jpg`.  

📌 **Что мы увидим?**  
Grok сгенерирует изображение **корабля**, например, вот такое:  

<img src="../../assets/ship.jpg" alt="Пример корабля" width="500">

🐹 Или, например, вы попросите "**Суслика на Эльбрусе**":

<img src="../../assets/gopher.jpg" alt="Суслик на Эльбрусе" width="500">

> 💡 **Фишка**: Вам не нужно вручную добывать cookies — клиент сделает это за вас!


---

## 🔧 Параметры запроса

Метод `GrokClient.ask` принимает множество параметров для настройки вашего запроса. Вот пример с настройками:

```python
from grok3api.client import GrokClient


client = GrokClient(history_msg_count=5, always_new_conversation=False) # для использования истории чата из серверов grok.com
client.history.set_main_system_prompt("Отвечай коротко и с эмодзи.")

# Отправляем запрос с настройками
result = client.ask(
    message="Нарисуй кота как на это картинке",
    modelName="grok-3",  # По умолчанию и так grok-3
    images=["C:\\Users\\user\\Downloads\\photo1_to_grok.jpg",
            "C:\\Users\\user\\Downloads\\photo2_to_grok.jpg"] # Вы можете отправлять несколько изображений Гроку!
)
print(f"Ответ Grok3: {result.modelResponse.message}")

# Сохраняем все изображения
for i, img in enumerate(result.modelResponse.generatedImages):
    img.save_to(f"cat_{i}.jpg")
    print(f"Сохранено: cat_{i}.jpg 🐾")
```

> 🌟 **Круто то, что это работает с автоматически полученными cookies!** Вам не нужно беспокоиться о доступе — клиент сам всё настроит.
 
 ---
 
 ## 🔄 Автоматическое получение cookies
 
 Если cookies отсутствуют или устарели, Grok3API автоматически:
 1. Использует браузер Chrome (главное, чтобы он был установлен).
 2. Посетит сайт `https://grok.com/`.
 3. Обойдёт защиту Cloudflare.
 4. Продолжит работу.
 
 Вам не нужно ничего делать вручную — просто запустите код, и всё заработает!

### [💼️ Описание класса `GrokClient`](ClientDoc.md)
### [✈️ Описание метода `ask`](askDoc.md)
### [📋 Описание класса `History`](HistoryDoc.md)
### [📬 Описание класса `GrokResponse`](GrokResponse.md)
### [🐧 Особенности работы с `Linux`](LinuxDoc.md)
### [🌐 Запуск OpenAI-совместимого сервера](OpenAI_Server.md)

---

## 🖼️ Удобное получение изображений

Одна из главных фишек GrokClient — это **супер-удобная работа со сгенерированными изображениями**. Вот полный пример:

```python
from grok3api.client import GrokClient

client = GrokClient()
result = client.ask("Нарисуй закат над морем")

for i, image in enumerate(result.modelResponse.generatedImages):
    image.save_to(f"sunset_{i}.jpg")
    print(f"Сохранено: sunset_{i}.jpg 🌅")
```


---


## 📋 Обработка ответов

Метод `ask` возвращает объект `GrokResponse`.

Поля объекта `GrokResponse`:
- **`modelResponse`**: Основной ответ модели.
  - `message` (str): Текстовый ответ.
  - `generatedImages` (List[GeneratedImage]): Список изображений.
- **`isThinking`**: Думала ли модель (bool).
- **`isSoftStop`**: Мягкая остановка (bool).
- **`responseId`**: ID ответа (str).
- **`newTitle`**: Новый заголовок чата, если есть (Optional[str]).

### [📬 Подробное описание класса `GrokResponse`](GrokResponse.md)

---


Если что-то неясно, пишите в issues — разберёмся вместе! 🌟


## Дисклеймер
Grok3API не имеет связи с xAI или разработчиками Grok. Это независимый проект, созданный третьей стороной, и он не поддерживается, не спонсируется и не одобряется xAI. Любые проблемы, связанные с Grok, должны решаться напрямую с xAI.
Вы несете ответственность за то, чтобы ваше использование Grok3API соответствовало всем применимым законам и регулированиям. Разработчик не поощряет незаконное использование.