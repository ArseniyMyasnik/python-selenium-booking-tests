from .base_page import  BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def should_be_opened_main_page(self):
        assert self.is_element_present(*MainPageLocators.WELCOME_MESSAGE)