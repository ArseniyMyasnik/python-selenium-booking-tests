import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from constants import UrlPage
from webdriver_manager.chrome import ChromeDriverManager
import contextlib
from pages.locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true', help='run without browser UI')
@pytest.fixture(scope='function')
def browser(request):
    headless = request.config.getoption('--headless')
    print('Configuring Chrome')
    chrome_options = ChromeOptions()
    if headless:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    yield browser
    print("\nquit browser")
    with contextlib.suppress(ConnectionResetError, OSError):
        browser.quit()


@pytest.fixture(scope='module')
def link_main_page(request):
    return UrlPage.URL_MAIN_PAGE

@pytest.fixture(scope='function')
def open_main_page(browser, link_main_page):
    browser.get(link_main_page)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(MainPageLocators.WELCOME_MESSAGE))
    yield browser, link_main_page
