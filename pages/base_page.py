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
