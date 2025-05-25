import asyncio
import json
from typing import Dict, List, Optional, Union
from enum import Enum
import base64
from io import BytesIO
import imghdr

from grok3api.logger import logger

try:
    import aiofiles
    AIOFILES_AVAILABLE = True
except ImportError:
    AIOFILES_AVAILABLE = False

class SenderType(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

class History:
    def __init__(self,
                 history_msg_count: int = 0,
                 history_path: str = "chat_histories.json",
                 history_as_json: bool = True,
                 main_system_prompt: str = None):
        self._chat_histories: Dict[str, List[Dict[str, Union[str, List[Dict[str, str]]]]]] = {}
        self.history_msg_count = history_msg_count
        self._system_prompts: Dict[str, str] = {}
        self.main_system_prompt: Optional[str] = main_system_prompt
        self.history_path = history_path
        self.history_as_json = history_as_json
        self.from_file()

    def set_main_system_prompt(self, text: str):
        try:
            self.main_system_prompt = text
        except Exception as e:
            logger.error(f"В set_main_system_prompt: {e}")

    def add_message(self, history_id: str,
                    sender_type: SenderType,
                    message: str):
        try:
            if self.history_msg_count < 0:
                self.history_msg_count = 0
            if history_id not in self._chat_histories:
                self._chat_histories[history_id] = []

            content = []
            if message:
                content.append({"type": "text", "text": message})

            new_message = {'role': sender_type.value, 'content': content}
            self._chat_histories[history_id].append(new_message)

            max_messages = self.history_msg_count + 1
            if len(self._chat_histories[history_id]) > max_messages:
                self._chat_histories[history_id] = self._chat_histories[history_id][-max_messages:]
        except Exception as e:
            logger.error(f"В add_message: {e}")

    def get_history(self, history_id: str) -> str:
        try:
            history = self._chat_histories.get(history_id, [])[:self.history_msg_count]

            if history_id not in self._system_prompts and self.main_system_prompt:
                history = [{'role': SenderType.SYSTEM.value, 'content': [{"type": "text", "text": self.main_system_prompt}]}] + history
            elif history_id in self._system_prompts:
                history = [{'role': SenderType.SYSTEM.value, 'content': [{"type": "text", "text": self._system_prompts[history_id]}]}] + history

            if self.history_as_json:
                return json.dumps(history, ensure_ascii=False)

            formatted_messages = []
            for msg in history:
                content = msg.get('content', '')
                text = ''

                if isinstance(content, str):
                    text = content
                elif isinstance(content, list):
                    for item in content:
                        if isinstance(item, dict) and item.get('type') == 'text':
                            text = item.get('text', '')
                            break

                formatted_line = f"{msg['role']}: {text}"
                formatted_messages.append(formatted_line)
            return "\n".join(formatted_messages)

        except Exception as e:
            logger.error(f"В get_history: {e}")
            return [] if self.history_as_json else ""

    def set_system_prompt(self, history_id: str, text: str):
        try:
            self._system_prompts[history_id] = text
        except Exception as e:
            logger.error(f"В set_system_prompt: {e}")

    def get_system_prompt(self, history_id: str) -> str:
        try:
            return self._system_prompts.get(history_id, "")
        except Exception as e:
            logger.error(f"В get_system_prompt: {e}")
            return ""

    def del_history_by_id(self, history_id: str) -> bool:
        """Deletes the chat history by `history_id`."""
        try:
            if history_id in self._chat_histories:
                del self._chat_histories[history_id]

            if history_id in self._system_prompts:
                del self._system_prompts[history_id]

            logger.debug(f"История с ID {history_id} удалена.")
            return True
        except Exception as e:
            logger.error(f"В delete_history: {e}")
            return False

    def to_file(self):
        try:
            with open(self.history_path, "w", encoding="utf-8") as file:
                json.dump({
                    "chat_histories": self._chat_histories,
                    "system_prompts": self._system_prompts,
                    "main_system_prompt": self.main_system_prompt
                }, file, ensure_ascii=False, indent=4)
        except Exception as e:
            logger.error(f"В save_history: {e}")

    async def async_to_file(self):
        """Asynchronously saves data to a file in JSON format."""
        try:
            data = {
                "chat_histories": self._chat_histories,
                "system_prompts": self._system_prompts,
                "main_system_prompt": self.main_system_prompt
            }
            if AIOFILES_AVAILABLE:
                async with aiofiles.open(self.history_path, "w", encoding="utf-8") as file:
                    await file.write(json.dumps(data, ensure_ascii=False, indent=4))
            else:
                def write_file_sync(path: str, content: dict):
                    with open(path, "w", encoding="utf-8") as file:
                        json.dump(content, file, ensure_ascii=False, indent=4)

                await asyncio.to_thread(write_file_sync, self.history_path, data)
        except Exception as e:
            logger.error(f"В to_file: {e}")

    def from_file(self):
        try:
            with open(self.history_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                self._chat_histories = data.get("chat_histories", {})
                self._system_prompts = data.get("system_prompts", {})
                self.main_system_prompt = data.get("main_system_prompt", None)
        except FileNotFoundError:
            logger.debug("В load_history: Файл не найден.")
        except Exception as e:
            logger.error(f"В load_history: {e}")


def encode_image(image: Union[str, BytesIO]) -> Optional[tuple[str, str]]:
    """Encodes an image in base64 and determines its type."""
    try:
        if isinstance(image, str):
            with open(image, "rb") as image_file:
                image_data = image_file.read()
        elif isinstance(image, BytesIO):
            image_data = image.getvalue()
        else:
            raise ValueError("Изображение должно быть путем к файлу или объектом BytesIO")

        image_type = imghdr.what(None, h=image_data)
        if not image_type:
            image_type = "jpeg"

        base64_image = base64.b64encode(image_data).decode('utf-8')
        return base64_image, image_type
    except FileNotFoundError:
        logger.error(f"В encode_image: Файл {image} не найден.")
        return None
    except Exception as e:
        logger.error(f"В encode_image: {e}")
        return None