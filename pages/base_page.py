from selenium.common.exceptions import WebDriverException, NoSuchElementException, \
    ElementNotInteractableException, NoSuchAttributeException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import inspect
import allure
from allure import attachment_type
import time
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.maximize_window()

    def open(self):
        try:
            self.browser.get(self.url)
        except WebDriverException:
            return False
        return True

    def refresh(self):
        self.browser.refresh()

    def is_element_present(self, type_selector, selector):
        self.browser.implicitly_wait(5)
        try:
            self.browser.find_element(type_selector, selector)
        except (NoSuchElementException or ElementNotInteractableException):
            return False
        return True

    def press_link(self, type_selector, selector):
        button = self.browser.find_element(type_selector, selector)
        button.click()

    def press_button(self, type_selector, selector):
        time.sleep(3)
        try:
            button = self.browser.find_element(type_selector, selector)
            button.click()
        except (NoSuchElementException or ElementNotInteractableException or type(button) == 'NoneType'):
            return False
        return True

    def set_value_input(self, type_selector, selector, data):
        try:
            input = self.browser.find_element(type_selector, selector)
            input.clear()
            input.send_keys(data)
        except NoSuchElementException:
            return False
        return True

    def scroll_to_element(self, type_selector, selector):
        element = self.browser.find_element(type_selector, selector)
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)

    def is_element_displayed(self, type_selector, selector):
        time.sleep(2)
        element = self.browser.find_element(type_selector, selector)
        is_displayed = self.browser.execute_script(
            "var elem = arguments[0];"
            "var rect = elem.getBoundingClientRect();"
            "return ("
            "rect.top >= 0 && rect.left >= 0 && "
            "rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && "
            "rect.right <= (window.innerWidth || document.documentElement.clientWidth));",
            element)
        return is_displayed

    def get_text_from_element(self, type_selector, selector):
        element = self.browser.find_element(type_selector, selector)
        return element.text

    def should_be_stub_error_message(self):
        assert self.is_element_present(*BasePageLocators.STUB_ERROR_MESSAGE)
