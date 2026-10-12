from selenium.common.exceptions import WebDriverException, NoSuchElementException, \
    ElementNotInteractableException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
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
        try:
            WebDriverWait(self.browser, 3).until(
                EC.presence_of_element_located((type_selector, selector))
            )
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException):
            return False
        return True

    def press_link(self, type_selector, selector):
        button = self.browser.find_element(type_selector, selector)
        button.click()

    def press_button(self, type_selector, selector,):
        try:
            button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((type_selector, selector))
            )
            button.click()
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException):
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

    def scroll_to_element(self, type_selector, selector, offset=0):
        element = self.browser.find_element(type_selector, selector)
        self.browser.execute_script('arguments[0].scrollIntoView({behavior: "instant", block: "start"});'
                                    f'window.scrollBy(0, {offset});'
                                    , element)

    def scroll_by_n_pixels(self, n):
        self.browser.execute_script(f'window.scrollBy(0, {n});')

    def is_element_displayed(self, type_selector, selector):
        try:
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((type_selector, selector)))
        except TimeoutException:
            return False
        return self.browser.execute_script(
            "var elem = arguments[0];"
            "var rect = elem.getBoundingClientRect();"
            "return ("
            "rect.top >= 0 && rect.left >= 0 && "
            "rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && "
            "rect.right <= (window.innerWidth || document.documentElement.clientWidth));",
            element)

    def get_text_from_element(self, type_selector, selector):
        element = self.browser.find_element(type_selector, selector)
        return element.text

    def should_be_stub_error_message(self):
        self.take_screenshot()
        assert self.is_element_present(*BasePageLocators.STUB_ERROR_MESSAGE)

    def take_screenshot(self):
        time.sleep(0.5)
        screenshot = self.browser.get_screenshot_as_png()
        allure.attach(
            screenshot,
            "Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
