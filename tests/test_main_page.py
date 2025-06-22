import pytest
import allure
import time
from pages.main_page import MainPage

@allure.description('Тесты главной страницы')
class TestMainPage():
    @allure.description('Тест открыта главная страница')
    def test_opened_main_page(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.should_be_opened_main_page()