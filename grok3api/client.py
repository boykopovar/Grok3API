import asyncio
import contextvars
import functools
import os
from asyncio import events
from typing import Optional, List, Union, Dict, Any, Tuple
import base64
import json
from io import BytesIO

from grok3api.history import History, SenderType
from grok3api import driver
from grok3api.logger import logger
from grok3api.types.GrokResponse import GrokResponse



class GrokClient:
    """
    Client for working with Grok.

    :param use_xvfb: Flag to use Xvfb. Defaults to True. Applicable only on Linux.
    :param proxy: (str) Proxy server URL, used only in cases of regional blocking.
    :param history_msg_count: Number of messages to keep in history (default is `0` — history saving is disabled).
    :param history_path: Path to the history file in JSON format. Default is "chat_histories.json".
    :param history_as_json: Whether to send history to Grok in JSON format (for history_msg_count > 0). Defaults to True.
    :param history_auto_save: Automatically overwrite history file after each message. Defaults to True.
    :param always_new_conversation: (bool) Whether to use the new chat creation URL when sending a request to Grok.
    :param conversation_id: (str) Grok chat ID. Use this to continue a conversation from where it left off. Must be used together with response_id.
    :param response_id: (str) Grok response ID in the conversation_id chat. Use this to continue a conversation from where it left off. Must be used together with conversation_id.
    :param timeout: Maximum time for client initialization. Default is 120 seconds.
    """

    NEW_CHAT_URL = "https://grok.com/rest/app-chat/conversations/new"
    CONVERSATION_URL = "https://grok.com/rest/app-chat/conversations/" # + {conversationId}/responses/
    max_tries: int = 5

    def __init__(self,
                 cookies: Union[Union[str, List[str]], Union[dict, List[dict]]] = None,
                 use_xvfb: bool = True,
                 proxy: Optional[str] = None,
                 history_msg_count: int = 0,
                 history_path: str = "chat_histories.json",
                 history_as_json: bool = True,
                 history_auto_save: bool = True,
                 always_new_conversation: bool = True,
                 conversation_id: Optional[str] = None,
                 response_id: Optional[str] = None,
                 enable_artifact_files: bool = False,
                 main_system_prompt: Optional[str] = None,
                 timeout: int = driver.web_driver.TIMEOUT):
        try:
            if (conversation_id is None) != (response_id is None):
                raise ValueError(
                    "If you want to use server history, you must provide both conversation_id and response_id.")

            self.cookies = cookies
            self.proxy = proxy
            self.use_xvfb: bool = use_xvfb
            self.history = History(history_msg_count=history_msg_count,
                                   history_path=history_path,
                                   history_as_json=history_as_json,
                                   main_system_prompt=main_system_prompt)
            self.history_auto_save: bool = history_auto_save
            self.proxy_index = 0
            self.enable_artifact_files = enable_artifact_files
            self.timeout: int = timeout

            self.always_new_conversation: bool = always_new_conversation
            self.conversationId: Optional[str] = conversation_id
            self.parentResponseId: Optional[str] = response_id
            self._statsig_id: Optional[str] = None

            driver.web_driver.init_driver(use_xvfb=self.use_xvfb, timeout=timeout, proxy=self.proxy)

            self._statsig_id = driver.web_driver.get_statsig()
        except Exception as e:
            logger.error(f"В GrokClient.__init__: {e}")
            raise e

    def _send_request(self,
                      payload,
                      headers,
                      timeout=driver.web_driver.TIMEOUT):
        try:
            """Отправляем запрос через браузер с таймаутом."""


            if not self._statsig_id:
                self._statsig_id = driver.web_driver.get_statsig()

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
                "x-statsig-id": self._statsig_id,
            })

            target_url = self.CONVERSATION_URL + self.conversationId + "/responses" if self.conversationId else self.NEW_CHAT_URL

            fetch_script = f"""
            const controller = new AbortController();
            const signal = controller.signal;
            setTimeout(() => controller.abort(), {timeout * 1000});

            const payload = {json.dumps(payload)};
            return fetch('{target_url}', {{
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
            # print(response)

            if isinstance(response, str) and response.startswith('Error:'):
                error_data = self.handle_str_error(response)
                if isinstance(error_data, dict):
                    return error_data

            if response and 'This service is not available in your region' in response:
                return 'This service is not available in your region'

            final_dict = {}
            conversation_info = {}
            new_title = None

            for line in response.splitlines():
                try:

                    parsed = json.loads(line)

                    if "modelResponse" in parsed.get("result", {}):
                        parsed["result"]["response"] = {"modelResponse": parsed["result"].pop("modelResponse")}

                    if "conversation" in parsed.get("result", {}):
                        conversation_info = parsed["result"]["conversation"]

                    if "title" in parsed.get("result", {}):
                        new_title = parsed["result"]["title"].get("newTitle")

                    if "modelResponse" in parsed.get("result", {}).get("response", {}):
                        final_dict = parsed
                    elif "modelResponse" in parsed.get("result", {}):
                        parsed["result"]["response"] = conversation_info
                except (json.JSONDecodeError, KeyError):
                    continue

            if final_dict:
                model_response = final_dict["result"]["response"]["modelResponse"]
                final_dict["result"]["response"] = {"modelResponse": model_response}
                final_dict["result"]["response"]["conversationId"] = conversation_info.get("conversationId")
                final_dict["result"]["response"]["title"] = conversation_info.get("title")
                final_dict["result"]["response"]["createTime"] = conversation_info.get("createTime")
                final_dict["result"]["response"]["modifyTime"] = conversation_info.get("modifyTime")
                final_dict["result"]["response"]["temporary"] = conversation_info.get("temporary")
                final_dict["result"]["response"]["newTitle"] = new_title

                if not self.always_new_conversation and model_response.get("responseId"):
                    self.conversationId = self.conversationId or conversation_info.get("conversationId")
                    self.parentResponseId = model_response.get("responseId") if self.conversationId else None

            logger.debug(f"Получили ответ: {final_dict}")
            return final_dict
        except Exception as e:
            logger.error(f"В _send_request: {e}")
            return {}

    IMAGE_SIGNATURES = {
        b'\xff\xd8\xff': ("jpg", "image/jpeg"),
        b'\x89PNG\r\n\x1a\n': ("png", "image/png"),
        b'GIF89a': ("gif", "image/gif")
    }

    def _is_base64_image(self, s: str) -> bool:
        try:
            decoded = base64.b64decode(s, validate=True)
            return any(decoded.startswith(sig) for sig in self.IMAGE_SIGNATURES)
        except Exception:
            return False

    def _get_extension_and_mime_from_header(self, data: bytes) -> Tuple[str, str]:
        for sig, (ext, mime) in self.IMAGE_SIGNATURES.items():
            if data.startswith(sig):
                return ext, mime
        return "jpg", "image/jpeg"

    def _upload_image(self,
                      file_input: Union[str, BytesIO],
                      file_extension: str = "jpg",
                      file_mime_type: str = None) -> str:
        """
        Uploads an image to the server from a file path or BytesIO and returns the fileMetadataId from the response.

        Args:
            file_input (Union[str, BytesIO]): File path or a BytesIO object containing the file content.
            file_extension (str): File extension without the dot (e.g., "jpg", "png"). Defaults to "jpg".
            file_mime_type (str): MIME type of the file. If None, it is determined automatically.

        Returns:
            str: fileMetadataId from the server response.

        Raises:
            ValueError: If the input data is invalid or the response does not contain fileMetadataId.
        """

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

        if file_extension is None or file_mime_type is None:
            ext, mime = self._get_extension_and_mime_from_header(file_content)
            file_extension = file_extension or ext
            file_mime_type = file_mime_type or mime

        file_content_b64 = base64.b64encode(file_content).decode("utf-8")
        file_name_base = file_content_b64[:10].replace("/", "_").replace("+", "_")
        file_name = f"{file_name_base}.{file_extension}"

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

        capcha = "Just a moment" in response
        if (isinstance(response, str) and response.startswith('Error:')) or capcha:
            if 'Too many requests' in response or 'Bad credentials' in response or capcha:
                driver.web_driver.restart_session()
                response = driver.web_driver.execute_script(fetch_script)
                if isinstance(response, str) and response.startswith('Error:'):
                    raise ValueError(response)
            else:
                raise ValueError(response)

        if not isinstance(response, dict) or "fileMetadataId" not in response:
            raise ValueError("Server response does not contain fileMetadataId")

        return response["fileMetadataId"]

    def _clean_conversation(self, payload: dict, history_id: str, message: str):
        if payload and "parentResponseId" in payload:
            del payload["parentResponseId"]
        payload["message"] = self._messages_with_possible_history(history_id, message)
        self.conversationId = None
        self.parentResponseId = None

    def _messages_with_possible_history(self, history_id: str, message: str) -> str:
        if (self.history.history_msg_count < 1 and self.history.main_system_prompt is None
                and history_id not in self.history._system_prompts):
            message_payload = message
        elif self.parentResponseId and self.conversationId:
            message_payload = message
        else:
            message_payload = self.history.get_history(history_id) + '\n' + message
        return message_payload


    def send_message(self,
                     message: str,
                     history_id: Optional[str] = None,
                     **kwargs: Any) -> GrokResponse:
        """Устаревший метод отправки сообщения. Please, use ask method."""
        logger.warning("Please, use GrokClient.ask method instead GrokClient.send_message")
        return self.ask(message=message,
                        history_id=history_id,
                        **kwargs)

    async def async_ask(self,
                        message: str,
                        history_id: Optional[str] = None,
                        new_conversation: bool = None,
                        timeout: Optional[int] = None,
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
        Asynchronous wrapper for the ask method.
        Sends a request to the Grok API with a single message and additional parameters.

        Args:
            message (str): The user message to send to the API.
            history_id (Optional[str]): Identifier to specify which chat history to use.
            new_conversation (Optional[bool]): Whether to use the new chat URL when sending the request to Grok (does not apply to the built-in History class).
            timeout (int): Timeout in seconds to wait for a response. Default is 360 or the value set during client creation.
            temporary (bool): Indicates if the session or request is temporary. Defaults to False.
            modelName (str): The AI model name for processing the request. Default is "grok-3".
            images (str / BytesIO / List[str / BytesIO]): Either a path to an image, a base64-encoded image, or BytesIO object (or a list of any of these types) to send. Should not be used with fileAttachments.
            fileAttachments (Optional[List[Dict[str, str]]]): List of file attachments. Each item is a string fileMetadataId.
            imageAttachments (Optional[List[Dict[str, str]]]): List of image attachments, similar to fileAttachments.
            customInstructions (str): Additional instructions or context for the model. Defaults to an empty string.
            deepsearch_preset (str): Preset for deep search. Defaults to an empty string.
            disableSearch (bool): Disable the model’s search functionality. Defaults to False.
            enableImageGeneration (bool): Enable image generation in the response. Defaults to True.
            enableImageStreaming (bool): Enable streaming of images. Defaults to True.
            enableSideBySide (bool): Enable side-by-side display of information. Defaults to True.
            imageGenerationCount (int): Number of images to generate. Defaults to 2.
            isPreset (bool): Indicates if the message is a preset. Defaults to False.
            isReasoning (bool): Enable reasoning mode in the model’s response. Defaults to False.
            returnImageBytes (bool): Return image data as bytes. Defaults to False.
            returnRawGrokInXaiRequest (bool): Return raw output from the model. Defaults to False.
            sendFinalMetadata (bool): Send final metadata with the request. Defaults to True.
            toolOverrides (Optional[Dict[str, Any]]): Dictionary to override tool settings. Defaults to an empty dictionary.

        Return:
            GrokResponse: The response from the Grok API as an object.
        """
        try:
            return await _to_thread(self.ask,
                                           message=message,
                                           history_id=history_id,
                                           new_conversation=new_conversation,
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
            return GrokResponse({}, self.enable_artifact_files)

    def ask(self,
            message: str,
            history_id: Optional[str] = None,
            new_conversation: bool = None,
            timeout: int = None,
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
        Sends a request to the Grok API with a single message and additional parameters.

        Args:
            message (str): The user message to send to the API.
            history_id (Optional[str]): Identifier to specify which chat history to use.
            new_conversation (Optional[bool]): Whether to use the new chat URL when sending the request to Grok (does not apply to the built-in History class).
            timeout (int): Timeout in seconds to wait for a response. Default is 360 or the value set during client creation.
            temporary (bool): Indicates if the session or request is temporary. Defaults to False.
            modelName (str): The AI model name for processing the request. Default is "grok-3".
            images (str / BytesIO / List[str / BytesIO]): Either a path to an image, a base64-encoded image, or BytesIO object (or a list of any of these types) to send. Should not be used with fileAttachments.
            fileAttachments (Optional[List[Dict[str, str]]]): List of file attachments. Each item is a string fileMetadataId.
            imageAttachments (Optional[List[Dict[str, str]]]): List of image attachments, similar to fileAttachments.
            customInstructions (str): Additional instructions or context for the model. Defaults to an empty string.
            deepsearch_preset (str): Preset for deep search. Defaults to an empty string.
            disableSearch (bool): Disable the model’s search functionality. Defaults to False.
            enableImageGeneration (bool): Enable image generation in the response. Defaults to True.
            enableImageStreaming (bool): Enable streaming of images. Defaults to True.
            enableSideBySide (bool): Enable side-by-side display of information. Defaults to True.
            imageGenerationCount (int): Number of images to generate. Defaults to 2.
            isPreset (bool): Indicates if the message is a preset. Defaults to False.
            isReasoning (bool): Enable reasoning mode in the model’s response. Defaults to False.
            returnImageBytes (bool): Return image data as bytes. Defaults to False.
            returnRawGrokInXaiRequest (bool): Return raw output from the model. Defaults to False.
            sendFinalMetadata (bool): Send final metadata with the request. Defaults to True.
            toolOverrides (Optional[Dict[str, Any]]): Dictionary to override tool settings. Defaults to an empty dictionary.

        Return:
            GrokResponse: The response from the Grok API as an object.
        """

        if timeout is None:
            timeout = self.timeout


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


            message_payload = self._messages_with_possible_history(history_id, message)

            payload = {
                "temporary": temporary,
                "modelName": modelName,
                "message": message_payload,
                "fileAttachments": fileAttachments if fileAttachments is not None else [],
                "forceConcise": True,
                "imageAttachments": imageAttachments if imageAttachments is not None else [],
                "customInstructions": customInstructions,
                "deepsearch preset": deepsearch_preset,
                "disableSearch": disableSearch,
                "disableTextFollowUps": True,
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
            if self.parentResponseId:
                payload["parentResponseId"] = self.parentResponseId

            logger.debug(f"Grok payload: {payload}")
            if new_conversation:
                self._clean_conversation(payload, history_id, message)

            statsig_try_index = 0
            statsig_try_max = 2
            safe_try_max = 4
            safe_try_index = 0
            try_index = 0
            response = ""
            use_cookies: bool = self.cookies is not None

            is_list_cookies = isinstance(self.cookies, list)

            while try_index < self.max_tries:
                logger.debug(
                    f"Попытка {try_index + 1} из {self.max_tries}" + (" (Without cookies)" if not use_cookies else ""))
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

                    if new_conversation:
                        self._clean_conversation(payload, history_id, message)

                    if safe_try_index > safe_try_max:
                        return GrokResponse(last_error_data, self.enable_artifact_files)
                    safe_try_index += 1
                    response = self._send_request(payload, headers, timeout)
                    logger.debug(f"Ответ Grok: {response}")

                    if response == {} and try_index != 0:
                        try_index += 1
                        driver.web_driver.close_driver()
                        driver.web_driver.init_driver()

                        self._clean_conversation(payload, history_id, message)

                        continue

                    if isinstance(response, dict) and response:
                        last_error_data = response
                        str_response = str(response)
                        if 'Too many requests' in str_response or 'credentials' in str_response:
                            self._clean_conversation(payload, history_id, message)
                            cookies_used += 1

                            if not is_list_cookies or cookies_used >= len(self.cookies) - 1:
                                self._clean_conversation(payload, history_id, message)
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
                                self._clean_conversation(payload, history_id, message)
                                self.cookies.append(self.cookies.pop(0))
                                continue

                        elif 'This service is not available in your region' in str_response:
                            return GrokResponse(last_error_data, self.enable_artifact_files)

                        elif 'a padding to disable MSIE and Chrome friendly error page' in str_response:
                            if not self.always_new_conversation:
                                last_error_data["error"] = "Can not bypass x-statsig-id protection. Try `always_new_conversation = True` to bypass x-statsig-id protection"
                                return GrokResponse(last_error_data, self.enable_artifact_files)

                            if statsig_try_index < statsig_try_max:
                                statsig_try_index += 1
                                self._statsig_id = driver.web_driver.get_statsig(restart_session=True)
                                continue

                            last_error_data["error"] = "Can not bypass x-statsig-id protection"
                            return GrokResponse(last_error_data, self.enable_artifact_files)

                        elif 'Just a moment' in str_response or '403' in str_response:
                            # driver.web_driver.close_driver()
                            # driver.web_driver.init_driver()
                            driver.web_driver.restart_session()
                            self._clean_conversation(payload, history_id, message)
                            break
                        else:
                            response = GrokResponse(response, self.enable_artifact_files)
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

                if try_index == self.max_tries - 1:
                    self._clean_conversation(payload, history_id, message)

                    driver.web_driver.close_driver()
                    driver.web_driver.init_driver()

                self._clean_conversation(payload, history_id, message)
                driver.web_driver.restart_session()

            logger.debug(f"(In ask) Bad response: {response}")
            driver.web_driver.restart_session()
            self._clean_conversation(payload, history_id, message)

            if not last_error_data:
                last_error_data = self.handle_str_error(response)

        except Exception as e:
            logger.debug(f"In ask: {e}")
            if not last_error_data:
                last_error_data = self.handle_str_error(str(e))
        finally:
            if self.history.history_msg_count > 0:
                self.history.add_message(history_id, SenderType.ASSISTANT, message)
                if self.history_auto_save:
                    self.history.to_file()
            return GrokResponse(last_error_data, self.enable_artifact_files)

    def handle_str_error(self, response_str):
        try:
            json_str = response_str.split(" - ", 1)[1]
            response = json.loads(json_str)

            if isinstance(response, dict):
                # {"error": {...}}
                if 'error' in response:
                    error = response['error']
                    error_code = error.get('code', 'Unknown')
                    error_message = error.get('message') or response_str
                    error_details = error.get('details') if isinstance(error.get('details'), list) else []
                # {"code": ..., "message": ..., "details": ...}
                elif 'message' in response:
                    error_code = response.get('code', 'Unknown')
                    error_message = response.get('message') or response_str
                    error_details = response.get('details') if isinstance(response.get('details'), list) else []
                else:
                    raise ValueError("Unsupported error format")

                return {
                    "error_code": error_code,
                    "error": error_message,
                    "details": error_details
                }

        except Exception:
            pass

        return {
            "error_code": "Unknown",
            "error": response_str,
            "details": []
        }

async def _to_thread(func, /, *args, **kwargs):

    loop = events.get_running_loop()
    ctx = contextvars.copy_context()
    func_call = functools.partial(ctx.run, func, *args, **kwargs)
    return await loop.run_in_executor(None, func_call)