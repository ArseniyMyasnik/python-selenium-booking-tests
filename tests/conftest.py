import os
import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from pages.base_page import BasePage
from constants import UrlPage
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true', help='запуск без интерфейса')
@pytest.fixture(scope='function')
def browser(request):
    headless = request.config.getoption('--headless')
    print('Настройка Chrome')
    chrome_options = ChromeOptions()
    if headless:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    yield browser
    print("\nquit browser")
    browser.quit()


@pytest.fixture(scope='module')
def link_main_page(request):
    return UrlPage.URL_MAIN_PAGE

@pytest.fixture(scope='function')
def open_main_page(browser, link_main_page):
    browser.get(link_main_page)
    browser.implicitly_wait(5)
    yield browser, link_main_page