from io import BytesIO
from dataclasses import dataclass
from typing import Optional, List

from grok3api.grok3api_logger import logger
from grok3api import driver


@dataclass
class GeneratedImage:
    url: str
    _base_url: str = "https://assets.grok.com"
    cookies: Optional[List[dict]] = None

    def __post_init__(self):
        """
        После инициализации проверяем driver.DRIVER и получаем куки для _base_url,
        если драйвер доступен. Иначе сохраняем cookies как None.
        """
        if driver.DRIVER is not None:
            self.cookies = driver.DRIVER.get_cookies()
        else:
            self.cookies = None

    def download(self, timeout: int = driver.TIMEOUT) -> Optional[BytesIO]:
        """Метод для загрузки изображения в память через браузер с таймаутом."""
        try:
            image_data = self._fetch_image(timeout=timeout)
            if image_data is None:
                return None
            return BytesIO(image_data)
        except Exception as e:
            logger.error(f"При загрузке изображения (download): {e}")
            return None

    def download_to(self, path: str, timeout: int = driver.TIMEOUT) -> None:
        """Скачивает изображение в файл через браузер с таймаутом."""
        try:
            image_data = self._fetch_image(timeout=timeout)
            if image_data is not None:
                with open(path, "wb") as f:
                    f.write(image_data)
                logger.debug(f"Изображение сохранено в: {path}")
            else:
                logger.debug("Изображение не загружено, сохранение отменено.")
        except Exception as e:
            logger.error(f"При загрузке в файл: {e}")

    def save_to(self, path: str, timeout: int = driver.TIMEOUT) -> None:
        """Скачивает изображение через download() и сохраняет его в файл с таймаутом."""
        try:
            logger.debug(f"Попытка сохранить изображение в файл: {path}")
            image_data = self.download(timeout=timeout)
            if image_data is not None:
                with open(path, "wb") as f:
                    f.write(image_data.getbuffer())
                logger.debug(f"Изображение успешно сохранено в: {path}")
            else:
                logger.debug("Изображение не было загружено, сохранение отменено.")
        except Exception as e:
            logger.error(f"В save_to: {e}")

    def _fetch_image(self, timeout: int = driver.TIMEOUT) -> Optional[bytes]:
        """Приватная функция для загрузки изображения через браузер с таймаутом."""
        if not self.cookies or len(self.cookies) == 0:
            logger.debug("Нет cookies для загрузки изображения.")
            return None

        image_url = self.url if self.url.startswith('/') else '/' + self.url
        full_url = self._base_url + image_url
        logger.debug(f"Полный URL для загрузки изображения: {full_url}, timeout: {timeout} сек")

        fetch_script = f"""
        const controller = new AbortController();
        const signal = controller.signal;
        const timeoutId = setTimeout(() => controller.abort(), {timeout * 1000});

        console.log("Starting fetch with credentials: 'include'");
        console.log("Cookies in browser before fetch:", document.cookie);

        const request = fetch('{full_url}', {{
            method: 'GET',
            signal: signal
        }})
        .then(response => {{
            clearTimeout(timeoutId);
            console.log("Response status:", response.status);
            console.log("Response headers:", Array.from(response.headers.entries()));
            const contentType = response.headers.get('Content-Type');
            if (!response.ok) {{
                console.log("Request failed with status:", response.status);
                return 'Error: HTTP ' + response.status;
            }}
            if (!contentType || !contentType.startsWith('image/')) {{
                return response.text().then(text => {{
                    console.log("Invalid MIME type detected:", contentType);
                    console.log("Response content:", text);
                    return 'Error: Invalid MIME type: ' + contentType + ', content: ' + text;
                }});
            }}
            return response.arrayBuffer();
        }})
        .then(buffer => {{
            console.log("Image data received, length:", buffer.byteLength);
            return Array.from(new Uint8Array(buffer));
        }})
        .catch(error => {{
            clearTimeout(timeoutId);
            console.log("Fetch error:", error.toString());
            return 'Error: ' + error;
        }});

        console.log("Fetch request sent, awaiting response...");
        return request;
        """
        driver.init_driver(wait_loading=False)
        try:
            try:
                for cookie in self.cookies:
                    if 'name' in cookie and 'value' in cookie:
                        if 'domain' not in cookie or not cookie['domain']:
                            cookie['domain'] = '.grok.com'
                        driver.DRIVER.add_cookie(cookie)
                    else:
                        logger.warning(f"Пропущена некорректная куки: {cookie}")
                logger.debug(f"Установлены куки: {self.cookies}")
            except Exception as e:
                logger.error(f"Ошибка при установке куки: {e}")
                return None

            driver.DRIVER.get(full_url)
            response = driver.DRIVER.execute_script(fetch_script)
            driver.DRIVER.get(driver.BASE_URL)
        except Exception as e:
            logger.error(f"Ошибка выполнения скрипта в браузере: {e}")
            return None

        if isinstance(response, str) and response.startswith('Error:'):
            logger.error(f"Ошибка при загрузке изображения: {response}")
            return None

        image_data = bytes(response)
        logger.debug("Изображение успешно загружено через браузер.")
        return image_data
