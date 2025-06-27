import pytest
import allure
import time
from pages.main_page import MainPage
from pages.locators import MainPageLocators

@allure.description('Тесты главной страницы')
class TestMainPage():
    @allure.description('MP-1: открыта главная страница')
    def test_opened_main_page(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        with allure.step('Результат: должна быть открыта главная страница'):
            page.should_be_opened_main_page()

    @allure.description('MP-2 - Кнопка "Book Now" прокручивает страницу до раздела "Our Rooms"')
    def test_press_book_now_button(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        with allure.step('Нажимаем кнопку "Book Now"'):
            page.press_button_book_now()
        with allure.step('Результат: страница прокрутилась до раздела "Our Rooms"'):
            page.should_be_displayed_header_our_rooms()

    @allure.description('MP-3.1 - Проверка доступности комнат, даты корректные')
    def test_set_correct_dates(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_header_check_dates()
        with allure.step('Нажимаем на кнопку "Check Availability"'):
            page.press_button_check_availability()
        with allure.step('Результат: свободные комнаты есть на корректные даты'):
            page.should_be_nth_room_card_displayed(cards_number=1)

    @allure.description('MP-3.2 - Проверка доступности комнат, дата въезда позже даты выезда')
    @pytest.mark.xfail(reason='Ожидается ошибка при дате въезда позже даты выезда, но её нет')
    def test_set_check_in_date_later_than_check_out(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_header_check_dates()
        with allure.step('Устанавливаем дату Check In = 15 числу будущего месяца'):
            page.set_calendar_date(date_type='check in', months_offset=1, day=15)
        with allure.step('Устанавливаем дату Check Out = 10 числу будущего месяца'):
            page.set_calendar_date(date_type='check out', months_offset=1, day=10)
        with allure.step('Нажимаем на кнопку "Check Availability"'):
            page.press_button_check_availability()
        with allure.step('Результат: появляется сообщение об ошибке в датах'):
            page.should_be_stub_error_message()

    @allure.description('MP-3.3 - Проверка доступности дат, даты устаревшие')
    @pytest.mark.xfail(reason='Ожидается ошибка при установке устаревших дат, но её нет')
    def test_set_past_dates(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_header_check_dates()
        with allure.step('Устанавливаем дату Check In = 1 числу прошлого месяца'):
            page.set_calendar_date(date_type='check in', months_offset=-1, day=1)
        with allure.step('Устанавливаем дату Check Out = 3 числу прошлого месяца'):
            page.set_calendar_date(date_type='check out', months_offset=-1, day=3)
        with allure.step('Нажимаем на кнопку "Check Availability"'):
            page.press_button_check_availability()
        with allure.step('Результат: появляется сообщение об ошибке в датах'):
            page.should_be_stub_error_message()
