import time

from .base_page import  BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

    def press_button_book_now(self):
        self.press_button(*MainPageLocators.BUTTON_BOOK_NOW), \
            'Кнопка не найдена'

    def press_button_check_availability(self):
        self.press_button(*MainPageLocators.BUTTON_CHECK_AVAILABILITY), \
            'Кнопка не найдена'

    def press_check_in_date(self):
        self.press_button(*MainPageLocators.CHECK_IN_DATE), \
            'Поле выбора Check In не видно на странице'

    def press_open_calendar(self, date_type):
        if date_type == 'check in':
            self.press_button(*MainPageLocators.CHECK_IN_DATE)
        elif date_type == 'check out':
            self.press_button(*MainPageLocators.CHECK_OUT_DATE)
        else:
            raise ValueError(f'На сайте нет поля выбора даты с названием {date_type}')

    def scroll_month(self, months_offset):
        if months_offset >= 0:
            for i in range(months_offset):
                self.press_button_next_month()
        elif months_offset < 0:
            for i in range(abs(months_offset)):
                self.press_button_previous_month()
        else:
            raise ValueError

    def press_on_the_day(self, day):
        current_month = self.get_current_month_year_from_calendar()[0]
        self.press_button(*MainPageLocators.get_select_nth_date_in_current_month_calendar(current_month, day)), \
            f'Похоже, в данном месяце нет {day} числа'

    def set_calendar_date(self, date_type, day, months_offset=0):
        self.press_open_calendar(date_type=date_type)
        self.scroll_month(months_offset=months_offset)
        self.press_on_the_day(day=day)

    def get_current_month_year_from_calendar(self):
        return self.get_text_from_element(*MainPageLocators.CURRENT_DATE_CALENDAR).split(" ")

    def press_button_next_month(self):
        self.press_button(*MainPageLocators.BUTTON_NEXT_MONTH), \
            'Кнопка не найдена'

    def press_button_previous_month(self):
        self.press_button(*MainPageLocators.BUTTON_PREVIOUS_MONTH), \
            'Кнопка не найдена'

    def scroll_to_header_check_dates(self):
        self.scroll_to_element(*MainPageLocators.HEADER_CHECK_DATES)

    def should_be_opened_main_page(self):
        assert self.is_element_present(*MainPageLocators.WELCOME_MESSAGE), \
            'Открыта не главная страница'
    def should_be_displayed_header_our_rooms(self):
        assert self.is_element_displayed(*MainPageLocators.HEADER_OUR_ROOMS), \
            'Заголовок "Our Rooms" не найден'

    def should_be_nth_room_card_displayed(self, cards_number):
        assert self.is_element_displayed(*MainPageLocators.get_select_of_nth_room_card(n=cards_number))