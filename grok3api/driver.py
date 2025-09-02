import logging
import random
import re
import string
import time
from typing import Optional
import os
import shutil
import subprocess
import atexit
import signal
import sys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import SessionNotCreatedException, TimeoutException

from grok3api.logger import logger

class WebDriverSingleton:
    """Синглтон для управления ChromeDriver."""
    _instance = None
    _driver: Optional[ChromeWebDriver] = None
    TIMEOUT = 360

    USE_XVFB = True
    xvfb_display: Optional[int] = None

    BASE_URL = "https://grok.com/"
    CHROME_VERSION = None
    WAS_FATAL = False
    def_proxy = "socks4://98.178.72.21:10919"

    execute_script = None
    add_cookie = None
    get_cookies = None
    get = None

    need_proxy: bool = False
    max_proxy_tries = 1
    proxy_try = 0
    proxy: Optional[str] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebDriverSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._hide_unnecessary_logs()
        self._patch_chrome_del()
        atexit.register(self.close_driver)
        signal.signal(signal.SIGINT, self._signal_handler)

    def _hide_unnecessary_logs(self):
        """Подавляет ненужные логи."""
        try:
            uc_logger = logging.getLogger("undetected_chromedriver")
            for handler in uc_logger.handlers[:]:
                uc_logger.removeHandler(handler)
            uc_logger.setLevel(logging.CRITICAL)

            selenium_logger = logging.getLogger("selenium")
            for handler in selenium_logger.handlers[:]:
                selenium_logger.removeHandler(handler)
            selenium_logger.setLevel(logging.CRITICAL)

            urllib3_con_logger = logging.getLogger("urllib3.connectionpool")
            for handler in urllib3_con_logger.handlers[:]:
                urllib3_con_logger.removeHandler(handler)
            urllib3_con_logger.setLevel(logging.CRITICAL)


            logging.getLogger("selenium.webdriver").setLevel(logging.CRITICAL)
            logging.getLogger("selenium.webdriver.remote.remote_connection").setLevel(logging.CRITICAL)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            logging.debug(f"Ошибка при подавлении логов (_hide_unnecessary_logs): {e}")

    def _patch_chrome_del(self):
        """Патчит метод __del__ для uc.Chrome."""
        def safe_del(self):
            try:
                try:
                    if hasattr(self, 'service') and self.service.process:
                        self.service.process.kill()
                        logger.debug("Процесс сервиса ChromeDriver успешно завершен.")
                except Exception as e:
                    logger.debug(f"Ошибка при завершении процесса сервиса: {e}")
                try:
                    self.quit()
                    logger.debug("ChromeDriver успешно закрыт через quit().")
                except Exception as e:
                    logger.debug(f"uc.Chrome.__del__: при вызове quit(): {e}")
            except Exception as e:
                logger.error(f"uc.Chrome.__del__: {e}")
        try:
            uc.Chrome.__del__ = safe_del
        except:
            pass

    def _is_driver_alive(self, driver):
        """Проверяет, живой ли драйвер."""
        try:
            driver.title
            return True
        except:
            return False

    def _setup_driver(self, driver, wait_loading: bool, timeout: int):
        """Настраивает драйвер: минимизирует, загружает базовый URL и ждет поле ввода."""
        self._minimize()

        driver.get(self.BASE_URL)
        patch_fetch_for_statsig(driver)

        page = driver.page_source
        if not page is None and isinstance(page, str) and 'This service is not available in your region' in page:
            if self.proxy_try > self.max_proxy_tries:
                raise ValueError("Cant bypass region block")

            self.need_proxy = True
            self.close_driver()
            self.init_driver(wait_loading=wait_loading, proxy=self.def_proxy)
            self.proxy_try += 1


        if wait_loading:
            logger.debug("Ждем загрузки страницы с неявным ожиданием...")
            try:
                WebDriverWait(driver, timeout).until(
                    ec.presence_of_element_located((By.CSS_SELECTOR, "div.relative.z-10 textarea"))
                )
                time.sleep(2)
                # statsig_id = driver.execute_script("""
                #     for (let key in localStorage) {
                #         if (key.startsWith('statsig.stable_id')) {
                #             return localStorage.getItem(key);
                #         }
                #     }
                #     return null;
                # """)
                # print(f"statsig.stable_id: {statsig_id}")
                self.proxy_try = 0
                logger.debug("Поле ввода найдено.")
            except Exception:
                logger.debug("Поле ввода не найдено")

    def init_driver(self, wait_loading: bool = True, use_xvfb: bool = True, timeout: Optional[int] = None, proxy: Optional[str] = None):
        """Запускает ChromeDriver и проверяет/устанавливает базовый URL с тремя попытками."""
        driver_timeout = timeout if timeout is not None else self.TIMEOUT
        self.TIMEOUT = driver_timeout
        if proxy is None:
            if self.need_proxy:
                proxy = self.def_proxy
        else:
            self.proxy = proxy

        self.USE_XVFB = use_xvfb
        attempts = 0
        max_attempts = 3

        def _create_driver():
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-dev-shm-usage")
            #chrome_options.add_argument("--auto-open-devtools-for-tabs")

            caps = DesiredCapabilities.CHROME
            caps['goog:loggingPrefs'] = {'browser': 'ALL'}

            if proxy:
                logger.debug(f"Добавляем прокси в опции: {proxy}")
                chrome_options.add_argument(f"--proxy-server={proxy}")

            new_driver = uc.Chrome(options=chrome_options, headless=False, use_subprocess=True, version_main=self.CHROME_VERSION, desired_capabilities=caps)
            new_driver.set_script_timeout(driver_timeout)
            return new_driver

        while attempts < max_attempts:
            try:
                if self.USE_XVFB:
                    self._safe_start_xvfb()

                if self._driver and self._is_driver_alive(self._driver):
                    self._minimize()
                    current_url = self._driver.current_url
                    if current_url != self.BASE_URL:
                        logger.debug(f"Текущий URL ({current_url}) не совпадает с базовым ({self.BASE_URL}), переходим...")
                        self._driver.get(self.BASE_URL)
                        if wait_loading:
                            logger.debug("Ждем загрузки страницы с неявным ожиданием...")
                            try:
                                WebDriverWait(self._driver, driver_timeout).until(
                                    ec.presence_of_element_located((By.CSS_SELECTOR, "div.relative.z-10 textarea"))
                                )
                                time.sleep(2)
                                wait_loading = False
                                logger.debug("Поле ввода найдено.")
                            except Exception:
                                logger.error("Поле ввода не найдено.")
                    self.WAS_FATAL = False
                    logger.debug("Драйвер живой, все ок.")

                    self.execute_script = self._driver.execute_script
                    self.add_cookie = self._driver.add_cookie
                    self.get_cookies = self._driver.get_cookies
                    self.get = self._driver.get

                    return

                logger.debug(f"Попытка {attempts + 1}: создаем новый драйвер...")

                self.close_driver()
                self._driver = _create_driver()
                self._setup_driver(self._driver, wait_loading, driver_timeout)
                self.WAS_FATAL = False

                logger.debug("Браузер запущен")

                self.execute_script = self._driver.execute_script
                self.add_cookie = self._driver.add_cookie
                self.get_cookies = self._driver.get_cookies
                self.get = self._driver.get

                return

            except SessionNotCreatedException as e:
                self.close_driver()
                error_message = str(e)
                match = re.search(r"Current browser version is (\d+)", error_message)
                if match:
                    current_version = int(match.group(1))
                else:
                    current_version = self._get_chrome_version()
                self.CHROME_VERSION = current_version
                logger.debug(f"Несовместимость браузера и драйвера, пробуем переустановить драйвер для Chrome {self.CHROME_VERSION}...")
                self._driver = _create_driver()
                self._setup_driver(self._driver, wait_loading, driver_timeout)
                logger.debug(f"Удалось установить версию драйвера на {self.CHROME_VERSION}.")
                self.WAS_FATAL = False

                self.execute_script = self._driver.execute_script
                self.add_cookie = self._driver.add_cookie
                return

            except Exception as e:
                logger.error(f"В попытке {attempts + 1}: {e}")
                attempts += 1
                self.close_driver()
                if attempts == max_attempts:
                    logger.fatal(f"Все {max_attempts} попыток неуспешны: {e}")
                    self.WAS_FATAL = True
                    raise e
                logger.debug("Ждем 1 секунду перед следующей попыткой...")
                time.sleep(1)


    def restart_session(self):
        """Перезапускает сессию, очищая куки, localStorage, sessionStorage и перезагружая страницу."""
        try:
            self._driver.delete_all_cookies()
            self._driver.execute_script("localStorage.clear();")
            self._driver.execute_script("sessionStorage.clear();")
            self._driver.get(self.BASE_URL)
            patch_fetch_for_statsig(self._driver)
            WebDriverWait(self._driver, self.TIMEOUT).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, "div.relative.z-10 textarea"))
            )
            time.sleep(2)
            logger.debug("Страница загружена, сессия обновлена.")
        except Exception as e:
            logger.debug(f"Ошибка при перезапуске сессии: {e}")

    def set_cookies(self, cookies_input):
        """Устанавливает куки в драйвере."""
        if cookies_input is None:
            return
        current_url = self._driver.current_url
        if not current_url.startswith("http"):
            raise Exception("Перед установкой куки нужно сначала открыть сайт в драйвере!")

        if isinstance(cookies_input, str):
            cookie_string = cookies_input.strip().rstrip(";")
            cookies = cookie_string.split("; ")
            for cookie in cookies:
                if "=" not in cookie:
                    continue
                name, value = cookie.split("=", 1)
                self._driver.add_cookie({
                    "name": name,
                    "value": value,
                    "path": "/"
                })
        elif isinstance(cookies_input, dict):
            if "name" in cookies_input and "value" in cookies_input:
                cookie = cookies_input.copy()
                cookie.setdefault("path", "/")
                self._driver.add_cookie(cookie)
            else:
                for name, value in cookies_input.items():
                    self._driver.add_cookie({
                        "name": name,
                        "value": value,
                        "path": "/"
                    })
        elif isinstance(cookies_input, list):
            for cookie in cookies_input:
                if isinstance(cookie, dict) and "name" in cookie and "value" in cookie:
                    cookie = cookie.copy()
                    cookie.setdefault("path", "/")
                    self._driver.add_cookie(cookie)
                else:
                    raise ValueError("Каждый словарь в списке должен содержать 'name' и 'value'")
        else:
            raise TypeError("cookies_input должен быть строкой, словарем или списком словарей")

    def close_driver(self):
        """Закрывает драйвер."""
        if self._driver:
            self._driver.quit()
            logger.debug("Браузер закрыт.")
        self._driver = None

    def set_proxy(self, proxy: str):
        """Меняет прокси в текущей сессии драйвера."""
        self.close_driver()
        self.init_driver(use_xvfb=self.USE_XVFB, timeout=self.TIMEOUT, proxy=proxy)

    def _minimize(self):
        """Минимизирует окно браузера."""
        try:
            self._driver.minimize_window()
        except Exception:
            pass

    def _safe_start_xvfb(self):
        """Запускает Xvfb на уникальном DISPLAY, и сохраняет его в переменную окружения."""
        if not sys.platform.startswith("linux"):
            return

        if shutil.which("Xvfb") is None:
            logger.error("Xvfb не установлен! Установите его командой: sudo apt install xvfb")
            raise RuntimeError("Xvfb отсутствует")

        if self.xvfb_display is None:
            display_number = 99
            while True:
                result = subprocess.run(["pgrep", "-f", f"Xvfb :{display_number}"], capture_output=True, text=True)
                if not result.stdout.strip():
                    break
                display_number += 1
            self.xvfb_display = display_number

        display_var = f":{self.xvfb_display}"
        os.environ["DISPLAY"] = display_var

        result = subprocess.run(["pgrep", "-f", f"Xvfb {display_var}"], capture_output=True, text=True)
        if result.stdout.strip():
            logger.debug(f"Xvfb уже запущен на дисплее {display_var}.")
            return

        logger.debug(f"Запускаем Xvfb на дисплее {display_var}...")
        subprocess.Popen(["Xvfb", display_var, "-screen", "0", "1024x768x24"],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        for _ in range(10):
            time.sleep(1)
            result = subprocess.run(["pgrep", "-f", f"Xvfb {display_var}"], capture_output=True, text=True)
            if result.stdout.strip():
                logger.debug(f"Xvfb успешно запущен на дисплее {display_var}.")
                return

        raise RuntimeError(f"Xvfb не запустился на дисплее {display_var} за 10 секунд!")

    def _get_chrome_version(self):
        """Определяет текущую версию Chrome."""
        if "win" in sys.platform.lower():
            try:
                import winreg
                reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
                    chrome_path, _ = winreg.QueryValueEx(key, "")

                output = subprocess.check_output([chrome_path, "--version"], shell=True, text=True).strip()
                version = re.search(r"(\d+)\.", output).group(1)
                return int(version)
            except Exception as e:
                logger.debug(f"Не удалось найти версию Chrome через реестр: {e}")

            chrome_paths = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            ]

            for path in chrome_paths:
                if os.path.exists(path):
                    try:
                        output = subprocess.check_output([path, "--version"], shell=True, text=True).strip()
                        version = re.search(r"(\d+)\.", output).group(1)
                        return int(version)
                    except Exception as e:
                        logger.debug(f"Ошибка при получении версии Chrome по пути {path}: {e}")
                        continue

            logger.error("Не удалось найти Chrome или его версию на Windows.")
            return None
        else:
            cmd = r'google-chrome --version'
            try:
                output = subprocess.check_output(cmd, shell=True, text=True).strip()
                version = re.search(r"(\d+)\.", output).group(1)
                return int(version)
            except Exception as e:
                logger.error(f"Ошибка при получении версии Chrome: {e}")
                return None

    def _signal_handler(self, sig, frame):
        """Обрабатывает сигналы для корректного завершения."""
        logger.debug("Остановка...")
        self.close_driver()
        sys.exit(0)

    def get_statsig(self, restart_session=False, try_index = 0) -> Optional[str]:
        if try_index > 3:
            return None
        statsig_id: Optional[str] = None
        try:
            statsig_id = self._update_statsig(restart_session)
        except Exception as e:
            logger.error(f"In get_statsig: {e}")
        finally:
            return statsig_id if statsig_id else self._update_statsig(True)

    def _initiate_answer(self):
        try:
            # news_button = WebDriverWait(self._driver, self.TIMEOUT).until(
            #     ec.element_to_be_clickable((By.CSS_SELECTOR, "button.inline-flex:has(svg.lucide-newspaper)"))
            # )
            # logger.debug("Кнопка новостей найдена")
            # self._driver.execute_script("arguments[0].click();", news_button)
            # logger.debug("Кнопка нажата, ждём ответа")
            textarea = WebDriverWait(self._driver, self.TIMEOUT).until(
                ec.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'relative')]//textarea"))
            )
            textarea.send_keys(random.choice(string.ascii_lowercase))
            textarea.send_keys(Keys.ENTER)
        except Exception as e:
            logger.error(f"In _initiate_answer: {e}")

    def _update_statsig(self, restart_session=False) -> Optional[str]:
        if restart_session:
            self.restart_session()
        current_url = self._driver.current_url

        if current_url != self.BASE_URL:
            logger.debug(f"Текущий URL {current_url} не совпадает с BASE_URL {self.BASE_URL}. Переход на BASE_URL.")
            self._driver.get(self.BASE_URL)
            patch_fetch_for_statsig(self._driver)
            logger.debug(f"Перешел на {self.BASE_URL}")

        self._initiate_answer()

        try:
            is_overlay_active = self._driver.execute_script("""
                const elements = document.querySelectorAll("p");
                for (const el of elements) {
                    if (el.textContent.includes("Making sure you're human")) {
                        const style = window.getComputedStyle(el);
                        if (style.visibility !== 'hidden' && style.display !== 'none') {
                            return true;
                        }
                    }
                }
                return false;
            """)

            if is_overlay_active:
                logger.debug("Обнаружен overlay с капчей — блокируем процесс.")
                return None


            WebDriverWait(self._driver, min(self.TIMEOUT, 20)).until(
                ec.any_of(
                    ec.presence_of_element_located((By.CSS_SELECTOR, "div.message-bubble p[dir='auto']")),
                    ec.presence_of_element_located((By.CSS_SELECTOR, "div.w-full.max-w-\\48rem\\]")),
                    ec.presence_of_element_located((By.XPATH, "//p[contains(text(), \"Making sure you're human...\")]"))
                )
            )

            if self._driver.find_elements(By.CSS_SELECTOR, "div.w-full.max-w-\\48rem\\]"):
                logger.debug("Ошибка подлинности")
                return None

            captcha_elements = self._driver.find_elements(By.XPATH,
                                                          "//p[contains(text(), \"Making sure you're human...\")]")
            if captcha_elements:
                logger.debug("Появилась капча 'Making sure you're human...'")
                return None

            logger.debug("Элемент ответа появился")
            statsig_id = self._driver.execute_script("return window.__xStatsigId;")
            logger.debug(f"Получен x-statsig-id: {statsig_id}")
            return statsig_id

        except TimeoutException:
            logger.debug("Ни ответа, ни ошибки, возвращаю None")
            return None
        except Exception as e:
            logger.debug(f"В _update_statsig: {e}")
            return None

    def del_captcha(self, timeout = 5):
        try:
            captcha_wrapper = WebDriverWait(self._driver, timeout).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, "div.main-wrapper"))
            )
            self._driver.execute_script("arguments[0].remove();", captcha_wrapper)
            return True
        except TimeoutException:
            return True
        except Exception as e:
            logger.debug(f"В del_captcha: {e}")
            return False



def patch_fetch_for_statsig(driver):
    result = driver.execute_script("""
        if (window.__fetchPatched) {
            return "fetch уже патчен";
        }

        window.__fetchPatched = false;
        const originalFetch = window.fetch;
        window.__xStatsigId = null;

        window.fetch = async function(...args) {
            console.log("➡️ Перехваченный fetch вызов с аргументами:", args);

            const response = await originalFetch.apply(this, args);

            try {
                const req = args[0];
                const opts = args[1] || {};
                const url = typeof req === 'string' ? req : req.url;
                const headers = opts.headers || {};

                const targetUrl = "https://grok.com/rest/app-chat/conversations/new";

                if (url === targetUrl) {
                    let id = null;
                    if (headers["x-statsig-id"]) {
                        id = headers["x-statsig-id"];
                    } else if (typeof opts.headers?.get === "function") {
                        id = opts.headers.get("x-statsig-id");
                    }

                    if (id) {
                        window.__xStatsigId = id;
                        console.log("✅ Сохранили x-statsig-id:", id);
                    } else {
                        console.warn("⚠️ x-statsig-id не найден в заголовках");
                    }
                } else {
                    console.log("ℹ️ Пропущен fetch, не совпадает с целевым URL:", url);
                }
            } catch (e) {
                console.warn("❌ Ошибка при извлечении x-statsig-id:", e);
            }

            return response;
        };

        window.__fetchPatched = true;
        return "fetch успешно патчен";
    """)
    # print(result)
    #
    # driver.execute_script("""
    #     fetch('https://grok.com/rest/app-chat/conversations/new', {
    #         headers: {'x-statsig-id': 'test123'}
    #     });
    # """)
    #
    # import time
    # time.sleep(1)
    #
    # statsig_id = driver.execute_script("return window.__xStatsigId;")
    # print("Captured x-statsig-id:", statsig_id)


web_driver = WebDriverSingleton()