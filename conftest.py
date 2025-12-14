import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# Добавляем параметр --language в командную строку
def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language: en, es, fr, de, etc."
    )


# Фикстура для запуска браузера с указанным языком
@pytest.fixture(scope="function")
def browser(request):
    # Получаем язык из командной строки
    user_language = request.config.getoption("--language")

    # Настройки Chrome
    chrome_options = ChromeOptions()
    chrome_options.add_argument(f"--lang={user_language}")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")  # Убери, если хочешь видеть браузер

    # Запускаем Chrome с нужным языком
    browser = webdriver.Chrome(options=chrome_options)

    # Устанавливаем неявное ожидание
    browser.implicitly_wait(10)

    yield browser

    # Закрываем браузер после теста
    browser.quit()
