import os
from grok3api.client import GrokClient


def main():
    client = GrokClient(history_msg_count=5)
    client.history.set_main_system_prompt("Представь что ты баскетболист")
    os.makedirs("images", exist_ok=True)
    while True:
        prompt = input("Ведите запрос: ")
        if prompt == "q": break
        result = client.send_message(prompt, "0")
        print(result.modelResponse.message)
        if result and result.modelResponse and result.modelResponse.generatedImages:
                image = result.modelResponse.generatedImages[0]
                image.save_to(f"images/gen_img.jpg")
        client.history.to_file()

if __name__ == '__main__':
    main()