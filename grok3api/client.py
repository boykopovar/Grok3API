import asyncio
import os
from typing import Optional, List, Union, Dict, Any
import base64
import json
from io import BytesIO

from grok3api.history import History, SenderType
from grok3api import driver
from grok3api.grok3api_logger import logger
from grok3api.types.GrokResponse import GrokResponse


class GrokClient:
    """
    Клиент для работы с Grok.

    :param use_xvfb: Флаг для использования Xvfb. По умолчанию True. Имеет значения только на Linux.
    :param proxy: (str) URL Прокси сервера, используется только в случае региональной блокировки.
    :param history_msg_count: Количество сообщений в истории (по умолчанию `0` - сохранение истории отключено).
    :param history_path: Путь к файлу с историей в JSON-формате. По умолчанию: "chat_histories.json"
    :param history_as_json: Отправить ли в Grok историю в формате JSON (для history_msg_count > 0). По умолчанию: True
    :param history_auto_save: Автоматическая перезапись истории в файл после каждого сообщения. По умолчанию: True
    :param timeout: Максимальное время на инициализацию клиента. По умолчанию: 120 секунд
    """

    NEW_CHAT_URL = "https://grok.com/rest/app-chat/conversations/new"

    def __init__(self,
                 cookies: Union[Union[str, List[str]], Union[dict, List[dict]]] = None,
                 use_xvfb: bool = True,
                 proxy: Optional[str] = None,
                 history_msg_count: int = 0,
                 history_path: str = "chat_histories.json",
                 history_as_json: bool = True,
                 history_auto_save: bool = True,
                 timeout: int = driver.web_driver.TIMEOUT):
        try:
            self.cookies = cookies
            self.proxy = proxy
            self.use_xvfb: bool = use_xvfb
            self.history = History(history_msg_count=history_msg_count,
                                   history_path=history_path,
                                   history_as_json=history_as_json)
            self.history_auto_save: bool = history_auto_save
            self.proxy_index = 0

            driver.web_driver.init_driver(use_xvfb=self.use_xvfb, timeout=timeout, proxy=self.proxy)
        except Exception as e:
            logger.error(f"В GrokClient.__init__: {e}")
            raise e

    def _send_request(self,
                      payload,
                      headers,
                      timeout=driver.web_driver.TIMEOUT):
        try:
            """Отправляем запрос через браузер с таймаутом."""

            headers.update({
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ru-RU,ru;q=0.9",
                "Content-Type": "application/json",
                "Origin": "https://grok.com",
                "Referer": "https://grok.com/",
                "Sec-Ch-Ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
            })

            fetch_script = f"""
            const controller = new AbortController();
            const signal = controller.signal;
            setTimeout(() => controller.abort(), {timeout * 1000});

            const payload = {json.dumps(payload)};
            return fetch('{self.NEW_CHAT_URL}', {{
                method: 'POST',
                headers: {json.dumps(headers)},
                body: JSON.stringify(payload),
                credentials: 'include',
                signal: signal
            }})
            .then(response => {{
                if (!response.ok) {{
                    return response.text().then(text => 'Error: HTTP ' + response.status + ' - ' + text);
                }}
                return response.text();
            }})
            .catch(error => {{
                if (error.name === 'AbortError') {{
                    return 'TimeoutError';
                }}
                return 'Error: ' + error;
            }});
            """

            response = driver.web_driver.execute_script(fetch_script)

            if isinstance(response, str) and response.startswith('Error:'):
                error_data = self.handle_str_error(response)
                if isinstance(error_data, dict):
                    return error_data

            if response and 'This service is not available in your region' in response:
                return 'This service is not available in your region'
            final_dict = {}
            for line in response.splitlines():
                try:
                    parsed = json.loads(line)
                    if "modelResponse" in parsed["result"]["response"]:
                        final_dict = parsed
                        break
                except (json.JSONDecodeError, KeyError):
                    continue
            logger.debug(f"Получили ответ: {final_dict}")
            return final_dict
        except Exception as e:
            logger.error(f"В _send_request: {e}")
            return {}

    def _is_base64_image(self, s: str) -> bool:
        try:
            decoded = base64.b64decode(s, validate=True)
            return (
                    decoded[:3] == b'\xff\xd8\xff' or  # JPEG
                    decoded[:8] == b'\x89PNG\r\n\x1a\n' or  # PNG
                    decoded[:6] == b'GIF89a'  # GIF
            )
        except Exception:
            return False

    def _upload_image(self,
                      file_input: Union[str, BytesIO],
                      file_extension: str = ".jpg",
                      file_mime_type: str = None) -> str:
        """
        Загружает изображение на сервер из пути к файлу или BytesIO и возвращает fileMetadataId из ответа.

        Args:
            file_input (Union[str, BytesIO]): Путь к файлу или объект BytesIO с содержимым файла.
            file_extension (str): Расширение файла (например, ".jpg", ".png"). По умолчанию ".jpg".
            file_mime_type (str): MIME-тип файла. Если None, определяется по расширению (по умолчанию "image/jpeg").

        Returns:
            str: fileMetadataId из ответа сервера.

        Raises:
            ValueError: Если входные данные некорректны или ответ не содержит fileMetadataId.
        """
        try:
            if isinstance(file_input, str):
                if os.path.exists(file_input):
                    with open(file_input, "rb") as f:
                        file_content = f.read()
                elif self._is_base64_image(file_input):
                    file_content = base64.b64decode(file_input)
                else:
                    raise ValueError("The string is neither a valid file path nor a valid base64 image string")
            elif isinstance(file_input, BytesIO):
                file_content = file_input.getvalue()
            else:
                raise ValueError("file_input must be a file path, a base64 string, or a BytesIO object")

            file_content_b64 = base64.b64encode(file_content).decode("utf-8")

            file_name_base = file_content_b64[:10].replace("/", "_").replace("+", "_")
            file_name = f"{file_name_base}{file_extension}"

            if file_mime_type is None:
                mime_types = {
                    ".jpg": "image/jpeg",
                    ".jpeg": "image/jpeg",
                    ".png": "image/png",
                    ".gif": "image/gif"
                }
                file_mime_type = mime_types.get(file_extension.lower(), "image/jpeg")

            b64_str_js_safe = json.dumps(file_content_b64)
            file_name_js_safe = json.dumps(file_name)
            file_mime_type_js_safe = json.dumps(file_mime_type)

            fetch_script = f"""
            return fetch('https://grok.com/rest/app-chat/upload-file', {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                    'Accept': '*/*',
                    'User-Agent': 'Mozilla/5.0',
                    'Origin': 'https://grok.com',
                    'Referer': 'https://grok.com/'
                }},
                body: JSON.stringify({{
                    fileName: {file_name_js_safe},
                    fileMimeType: {file_mime_type_js_safe},
                    content: {b64_str_js_safe}
                }}),
                credentials: 'include'
            }})
            .then(response => {{
                if (!response.ok) {{
                    return response.text().then(text => 'Error: HTTP ' + response.status + ' - ' + text);
                }}
                return response.json();
            }})
            .catch(error => 'Error: ' + error);
            """

            response = driver.web_driver.execute_script(fetch_script)

            if isinstance(response, str) and response.startswith('Error:'):
                if 'Too many requests' in response or 'Bad credentials' in response:
                    driver.web_driver.restart_session()
                    response = driver.web_driver.execute_script(fetch_script)
                    if isinstance(response, str) and response.startswith('Error:'):
                        raise ValueError(f"File upload error: {response}")
                raise ValueError(f"File upload error: {response}")

            if not isinstance(response, dict) or "fileMetadataId" not in response:
                raise ValueError("Server response does not contain fileMetadataId")

            return response["fileMetadataId"]

        except Exception as e:
            raise ValueError(f"Failed to upload image: {e}")


    def send_message(self,
                     message: str,
                     history_id: Optional[str] = None,
                     proxy: Optional[str] = driver.web_driver.def_proxy,
                     **kwargs: Any) -> GrokResponse:
        """Устаревший метод отправки сообщения. Используйте ask() напрямую."""

        return self.ask(message=message,
                        history_id=history_id,
                        proxy=proxy,
                        **kwargs)

    async def async_ask(self,
                        message: str,
                        history_id: Optional[str] = None,
                        proxy: Optional[str] = driver.web_driver.def_proxy,
                        timeout: int = driver.web_driver.TIMEOUT,
                        temporary: bool = False,
                        modelName: str = "grok-3",
                        images: Union[Optional[List[Union[str, BytesIO]]], str, BytesIO] = None,
                        fileAttachments: Optional[List[str]] = None,
                        imageAttachments: Optional[List] = None,
                        customInstructions: str = "",
                        deepsearch_preset: str = "",
                        disableSearch: bool = False,
                        enableImageGeneration: bool = True,
                        enableImageStreaming: bool = True,
                        enableSideBySide: bool = True,
                        imageGenerationCount: int = 2,
                        isPreset: bool = False,
                        isReasoning: bool = False,
                        returnImageBytes: bool = False,
                        returnRawGrokInXaiRequest: bool = False,
                        sendFinalMetadata: bool = True,
                        toolOverrides: Optional[Dict[str, Any]] = None) -> GrokResponse:
        """
        Асинхронная обёртка метода ask.
        Отправляет запрос к API Grok с одним сообщением и дополнительными параметрами.

        Args:
            message (str): Сообщение пользователя для отправки в API.
            history_id (Optional[str]): Идентификатор для определения, какую историю чата использовать.
            proxy (Optional[str]): URL прокси-сервера, используется только в случае региональной блокировки.
            timeout (int): Таймаут (в секундах) на ожидание ответа. По умолчанию: 120.
            temporary (bool): Указывает, является ли сессия или запрос временным. По умолчанию False.
            modelName (str): Название модели ИИ для обработки запроса. По умолчанию "grok-3".
            images (str / BytesIO / List[str / BytesIO]): Или путь к изображению, или base64-кодированное изображение, или BytesIO (можно список любого из перечисленных типов) для отправки. Не должно быть использовано fileAttachments.
            fileAttachments (Optional[List[Dict[str, str]]]): Список вложений файлов. Каждый элемент — строка fileMetadataId.
            imageAttachments (Optional[List[Dict[str, str]]]): Список вложений изображений, аналогично fileAttachments.
            customInstructions (str): Дополнительные инструкции или контекст для модели. По умолчанию пустая строка.
            deepsearch_preset (str): Предустановка для глубокого поиска. По умолчанию пустая строка.
            disableSearch (bool): Отключить функцию поиска модели. По умолчанию False.
            enableImageGeneration (bool): Включить генерацию изображений в ответе. По умолчанию True.
            enableImageStreaming (bool): Включить потоковую передачу изображений. По умолчанию True.
            enableSideBySide (bool): Включить отображение информации бок о бок. По умолчанию True.
            imageGenerationCount (int): Количество генерируемых изображений. По умолчанию 2.
            isPreset (bool): Указывает, является ли сообщение предустановленным. По умолчанию False.
            isReasoning (bool): Включить режим рассуждений в ответе модели. По умолчанию False.
            returnImageBytes (bool): Возвращать данные изображений в виде байтов. По умолчанию False.
            returnRawGrokInXaiRequest (bool): Возвращать необработанный вывод от модели. По умолчанию False.
            sendFinalMetadata (bool): Отправлять финальные метаданные с запросом. По умолчанию True.
            toolOverrides (Optional[Dict[str, Any]]): Словарь для переопределения настроек инструментов. По умолчанию пустой словарь.

        Return:
            GrokResponse: Ответ от API Grok в виде объекта.
        """
        try:
            return await asyncio.to_thread(self.ask,
                                           message=message,
                                           history_id=history_id,
                                           proxy=proxy,
                                           timeout=timeout,
                                           temporary=temporary,
                                           modelName=modelName,
                                           images=images,
                                           fileAttachments=fileAttachments,
                                           imageAttachments=imageAttachments,
                                           customInstructions=customInstructions,
                                           deepsearch_preset=deepsearch_preset,
                                           disableSearch=disableSearch,
                                           enableImageGeneration=enableImageGeneration,
                                           enableImageStreaming=enableImageStreaming,
                                           enableSideBySide=enableSideBySide,
                                           imageGenerationCount=imageGenerationCount,
                                           isPreset=isPreset,
                                           isReasoning=isReasoning,
                                           returnImageBytes=returnImageBytes,
                                           returnRawGrokInXaiRequest=returnRawGrokInXaiRequest,
                                           sendFinalMetadata=sendFinalMetadata,
                                           toolOverrides=toolOverrides)
        except Exception as e:
            logger.error(f"In async_ask: {e}")
            return GrokResponse({})

    def ask(self,
            message: str,
            history_id: Optional[str] = None,
            proxy: Optional[str] = driver.web_driver.def_proxy,
            timeout: int = 120,
            temporary: bool = False,
            modelName: str = "grok-3",
            images: Union[Optional[List[Union[str, BytesIO]]], str, BytesIO] = None,
            fileAttachments: Optional[List[str]] = None,
            imageAttachments: Optional[List] = None,
            customInstructions: str = "",
            deepsearch_preset: str = "",
            disableSearch: bool = False,
            enableImageGeneration: bool = True,
            enableImageStreaming: bool = True,
            enableSideBySide: bool = True,
            imageGenerationCount: int = 2,
            isPreset: bool = False,
            isReasoning: bool = False,
            returnImageBytes: bool = False,
            returnRawGrokInXaiRequest: bool = False,
            sendFinalMetadata: bool = True,
            toolOverrides: Optional[Dict[str, Any]] = None
            ) -> GrokResponse:
        """
        Отправляет запрос к API Grok с одним сообщением и дополнительными параметрами.

        Args:
            message (str): Сообщение пользователя для отправки в API.
            history_id (Optional[str]): Идентификатор для определения, какую историю чата использовать.
            proxy (Optional[str]): URL прокси-сервера, используется только в случае региональной блокировки.
            timeout (int): Таймаут (в секундах) на ожидание ответа. По умолчанию: 120.
            temporary (bool): Указывает, является ли сессия или запрос временным. По умолчанию False.
            modelName (str): Название модели ИИ для обработки запроса. По умолчанию "grok-3".
            images (str / BytesIO / List[str / BytesIO]): Или путь к изображению, или base64-кодированное изображение, или BytesIO (можно список любого из перечисленных типов) для отправки. Не должно быть использовано fileAttachments.
            fileAttachments (Optional[List[Dict[str, str]]]): Список вложений файлов. Каждый элемент — строка fileMetadataId.
            imageAttachments (Optional[List[Dict[str, str]]]): Список вложений изображений, аналогично fileAttachments.
            customInstructions (str): Дополнительные инструкции или контекст для модели. По умолчанию пустая строка.
            deepsearch_preset (str): Предустановка для глубокого поиска. По умолчанию пустая строка.
            disableSearch (bool): Отключить функцию поиска модели. По умолчанию False.
            enableImageGeneration (bool): Включить генерацию изображений в ответе. По умолчанию True.
            enableImageStreaming (bool): Включить потоковую передачу изображений. По умолчанию True.
            enableSideBySide (bool): Включить отображение информации бок о бок. По умолчанию True.
            imageGenerationCount (int): Количество генерируемых изображений. По умолчанию 2.
            isPreset (bool): Указывает, является ли сообщение предустановленным. По умолчанию False.
            isReasoning (bool): Включить режим рассуждений в ответе модели. По умолчанию False.
            returnImageBytes (bool): Возвращать данные изображений в виде байтов. По умолчанию False.
            returnRawGrokInXaiRequest (bool): Возвращать необработанный вывод от модели. По умолчанию False.
            sendFinalMetadata (bool): Отправлять финальные метаданные с запросом. По умолчанию True.
            toolOverrides (Optional[Dict[str, Any]]): Словарь для переопределения настроек инструментов. По умолчанию пустой словарь.

        Return:
            GrokResponse: Ответ от API Grok в виде объекта.
        """
        if images is not None and fileAttachments is not None:
            raise ValueError("'images' and 'fileAttachments' cannot be used together")
        last_error_data = {}
        try:
            base_headers = {
                "Content-Type": "application/json",
                "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                               "(KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"),
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "ru-RU,ru;q=0.9",
                "Origin": "https://grok.com",
                "Referer": "https://grok.com/",
            }

            headers = base_headers.copy()

            if images:
                fileAttachments = []
                if isinstance(images, list):
                    for image in images:
                        fileAttachments.append(self._upload_image(image))
                else:
                    fileAttachments.append(self._upload_image(images))


            if (self.history.history_msg_count < 1 and self.history.main_system_prompt is None
                    and history_id not in self.history.system_prompts):
                message_payload = message
            else:
                message_payload = self.history.get_history(history_id) + '\n' + message
                if self.history.history_msg_count > 0:
                    self.history.add_message(history_id, SenderType.ASSISTANT, message)
                    if self.history_auto_save:
                        self.history.to_file()

            payload = {
                "temporary": temporary,
                "modelName": modelName,
                "message": message_payload,
                "fileAttachments": fileAttachments if fileAttachments is not None else [],
                "imageAttachments": imageAttachments if imageAttachments is not None else [],
                "customInstructions": customInstructions,
                "deepsearch preset": deepsearch_preset,
                "disableSearch": disableSearch,
                "enableImageGeneration": enableImageGeneration,
                "enableImageStreaming": enableImageStreaming,
                "enableSideBySide": enableSideBySide,
                "imageGenerationCount": imageGenerationCount,
                "isPreset": isPreset,
                "isReasoning": isReasoning,
                "returnImageBytes": returnImageBytes,
                "returnRawGrokInXaiRequest": returnRawGrokInXaiRequest,
                "sendFinalMetadata": sendFinalMetadata,
                "toolOverrides": toolOverrides if toolOverrides is not None else {}
            }

            logger.debug(f"Grok payload: {payload}")

            max_tries = 5
            try_index = 0
            response = ""
            use_cookies: bool = self.cookies is not None

            is_list_cookies = isinstance(self.cookies, list)

            while try_index < max_tries:
                logger.debug(
                    f"Попытка {try_index + 1} из {max_tries}" + (" (Without cookies)" if not use_cookies else ""))
                cookies_used = 0

                while cookies_used < (len(self.cookies) if is_list_cookies else 1) or not use_cookies:
                    if use_cookies:
                        current_cookies = self.cookies[0] if is_list_cookies else self.cookies
                        driver.web_driver.set_cookies(current_cookies)
                        if images:
                            fileAttachments = []
                            if isinstance(images, list):
                                for image in images:
                                    fileAttachments.append(self._upload_image(image))
                            else:
                                fileAttachments.append(self._upload_image(images))
                            payload["fileAttachments"] = fileAttachments if fileAttachments is not None else []

                    logger.debug(
                        f"Отправляем запрос (cookie[{cookies_used}]): headers={headers}, payload={payload}, timeout={timeout} секунд")
                    response = self._send_request(payload, headers, timeout)

                    if isinstance(response, dict) and response:
                        last_error_data = response
                        str_response = str(response)
                        if 'Too many requests' in str_response or 'Bad credentials' in str_response:
                            cookies_used += 1

                            if not is_list_cookies or cookies_used >= len(self.cookies) - 1:
                                driver.web_driver.restart_session()
                                use_cookies = False
                                if images:
                                    fileAttachments = []
                                    if isinstance(images, list):
                                        for image in images:
                                            fileAttachments.append(self._upload_image(image))
                                    else:
                                        fileAttachments.append(self._upload_image(images))
                                    payload["fileAttachments"] = fileAttachments if fileAttachments is not None else []
                                continue
                            if is_list_cookies and len(self.cookies) > 1:
                                self.cookies.append(self.cookies.pop(0))
                                continue

                        elif 'This service is not available in your region' in str_response:
                            driver.web_driver.set_proxy(proxy)
                            break
                        elif 'Just a moment' in str_response or '403' in str_response:
                            driver.web_driver.close_driver()
                            driver.web_driver.init_driver()
                            break
                        else:
                            response = GrokResponse(response)
                            assistant_message = response.modelResponse.message

                            if self.history.history_msg_count > 0:
                                self.history.add_message(history_id, SenderType.ASSISTANT, assistant_message)
                                if self.history_auto_save:
                                    self.history.to_file()

                            return response
                    else:
                        break

                if is_list_cookies and cookies_used >= len(self.cookies):
                    break

                try_index += 1

                if try_index == max_tries - 1:
                    driver.web_driver.close_driver()
                    driver.web_driver.init_driver()

                driver.web_driver.restart_session()

            logger.error(f"(In ask) Bad response: {response}")
            driver.web_driver.restart_session()
            return GrokResponse(last_error_data)
        except Exception as e:
            logger.error(f"In ask: {e}")
            return GrokResponse(last_error_data)

    def handle_str_error(self, response_str):
        try:
            json_str = response_str.split(" - ")[1]
            response = json.loads(json_str)
            if isinstance(response, dict) and 'error' in response:
                error_code = response['error'].get('code')
                error_message = response['error'].get('message', 'Unknown error')
                error_details = response['error'].get('details', [])

                error_data = {
                    "error_code": error_code,
                    "error": error_message,
                    "details": error_details,
                }
                return error_data

        except Exception:
            return {"error_code": "Unknown", "error": response_str, "details": []}