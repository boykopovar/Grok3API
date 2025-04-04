import asyncio
import os
from grok3api.client import GrokClient

cookies_dict = {
    "i18nextLng": "ru",
    "sso-rw": "sso-rw-token-placeholder",
    "sso": "sso-token-placeholder",
    "cf_clearance": "cf_clearance-placeholder",
    "_ga": "ga-placeholder",
    "_ga_8FEWB057YH": "ga-8FEWB057YH-placeholder"
}

cookie_str = (
    "i18nextLng=ru; sso-rw=sso-rw-token-placeholder; sso=sso-token-placeholder; cf_clearance=cf_clearance-placeholder; _ga=ga-placeholder; _ga_8FEWB057YH=ga-8FEWB057YH-placeholder"
)

async def main():
    client = GrokClient(history_msg_count=5, cookies=cookie_str) # You can use str or dict format
    client.history.set_main_system_prompt("Отвечай коротко и с эмодзи.")
    os.makedirs("images", exist_ok=True)
    while True:
        prompt = input("Ведите запрос: ")
        if prompt == "q": break
        result = await client.async_ask(message=prompt, modelName="grok-3", history_id="0")
        if result.error:
            print(f"Произошла ошибка: {result.error}")
            continue
        print(result.modelResponse.message)
        if result.modelResponse.generatedImages:
            for index, image in enumerate(result.modelResponse.generatedImages, start=1):
                await image.async_save_to(f"images/gen_img_{index}.jpg")
        await client.history.async_to_file()

if __name__ == '__main__':
    asyncio.run(main())