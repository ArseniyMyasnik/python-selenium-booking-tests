import time

from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasePageLocators

class MainPage(BasePage):

    def press_button_book_now(self):
        assert self.press_button(*MainPageLocators.BUTTON_BOOK_NOW), \
            'Кнопка "Book Now" не найдена'

    def press_button_check_availability(self):
        self.take_screenshot()
        assert self.press_button(*MainPageLocators.BUTTON_CHECK_AVAILABILITY), \
            'Кнопка "Check Availability" не найдена'

    def press_check_in_date(self):
        assert self.press_button(*MainPageLocators.CHECK_IN_DATE), \
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
        assert self.press_button(*MainPageLocators.get_select_nth_date_in_current_month_calendar(current_month, day)), \
            f'Похоже, в данном месяце нет {day} числа'

    def set_calendar_date(self, date_type, day, months_offset=0):
        self.press_open_calendar(date_type=date_type)
        self.scroll_month(months_offset=months_offset)
        self.press_on_the_day(day=day)

    def get_current_month_year_from_calendar(self):
        return self.get_text_from_element(*MainPageLocators.CURRENT_DATE_CALENDAR).split(" ")

    def press_button_next_month(self):
        assert self.press_button(*MainPageLocators.BUTTON_NEXT_MONTH), \
            'Кнопка следующего месяца не найдена'

    def press_button_previous_month(self):
        assert self.press_button(*MainPageLocators.BUTTON_PREVIOUS_MONTH), \
            'Кнопка предыдущего месяца не найдена'

    def input_name(self, name):
        self.take_screenshot()
        self.set_value_input(*MainPageLocators.INPUT_NAME, data=name)

    def input_email(self, email):
        self.take_screenshot()
        self.set_value_input(*MainPageLocators.INPUT_EMAIL, data=email)

    def input_phone(self, phone):
        self.take_screenshot()
        self.set_value_input(*MainPageLocators.INPUT_PHONE, data=phone)

    def input_subject(self, subject):
        self.take_screenshot()
        self.set_value_input(*MainPageLocators.INPUT_SUBJECT, data=subject)

    def input_message(self, message):
        self.take_screenshot()
        self.set_value_input(*MainPageLocators.INPUT_MESSAGE, data=message)

    def scroll_to_header_check_dates(self):
        self.take_screenshot()
        self.scroll_to_element(*MainPageLocators.HEADER_CHECK_DATES)

    def scroll_to_header_send_us_a_message(self):
        self.scroll_to_element(*MainPageLocators.HEADER_SEND_US_A_MESSAGE)

    def scroll_to_submit_send_us_a_message_form(self):
        self.scroll_to_element(*MainPageLocators.SUBMIT_SEND_US_A_MESSAGE_FORM)

    def press_submit_send_us_a_message_form(self):
        self.scroll_to_element(*MainPageLocators.SUBMIT_SEND_US_A_MESSAGE_FORM)
        self.press_button(*MainPageLocators.SUBMIT_SEND_US_A_MESSAGE_FORM)
        self.take_screenshot()

    def should_be_opened_main_page(self):
        self.take_screenshot()
        assert self.is_element_present(*MainPageLocators.WELCOME_MESSAGE), \
            'Открыта не главная страница'
    def should_be_displayed_header_our_rooms(self):
        self.take_screenshot()
        assert self.is_element_displayed(*MainPageLocators.HEADER_OUR_ROOMS), \
            'Заголовок "Our Rooms" не найден'

    def should_be_nth_room_card_displayed(self, cards_number):
        self.take_screenshot()
        assert self.is_element_displayed(*MainPageLocators.get_select_of_nth_room_card(n=cards_number)), \
            f'{cards_number}-я карточка отсутствует'

    def check_error_name_is_blank_present(self, should_be_present):
        is_present = self.is_element_present(*MainPageLocators.ERROR_NAME_IS_BLANK)
        if should_be_present:
            assert is_present, \
                'Ошибка "Name may not be blank" отсутствует'
        else:
            assert not is_present, \
                'Ошибка "Name may not be blank" не должна присутствовать'

    def check_error_name_wrong_format_present(self, should_be_present):
        is_present = self.is_element_present(*BasePageLocators.STUB_ERROR_MESSAGE)
        if should_be_present:
            assert is_present, \
                'Ошибка "must be a well-formed name" отсутствует'
        else:
            assert not is_present, \
                'Ошибка "must be a well-formed name" не должна присутствовать'

    def check_error_email_is_blank_present(self, should_be_present):
        is_present = self.is_element_present(*MainPageLocators.ERROR_EMAIL_IS_BLANK)
        if should_be_present:
            assert is_present, \
                'Ошибка "Email may not be blank" отсутствует'
        else:
            assert not is_present, \
                'Ошибка "Email may not be blank" не должна присутствовать'

    def check_error_email_wrong_format_present(self, should_be_present):
        self.take_screenshot()
        is_present = self.is_element_present(*MainPageLocators.ERROR_EMAIL_WRONG_FORM)
        if should_be_present:
            assert is_present, \
                'Ошибка "must be a well-formed email address" отсутствует'
        else:
            assert not is_present, \
                'Ошибка "must be a well-formed email address" не должна присутствовать'

    def check_error_phone_is_blank_present(self, should_be_present):
        is_present = self.is_element_present(*MainPageLocators.ERROR_PHONE_IS_BLANK)
        if should_be_present:
            assert is_present, \
                'Ошибка "Phone may not be blank" отсутствует'
        else:
            assert not is_present, \
                'Ошибка "Phone may not be blank" не должна присутствовать'

    def check_error_phone_wrong_length_present(self, should_be_present):
        is_present = self.is_element_present(*MainPageLocators.ERROR_PHONE_WRONG_LENGTH)
        if should_be_present:
            assert is_present, \
                'Ошибка "Phone must be between 11 and 21 characters." отсутствует'
        else:
            assert not is_present, \
                'Ошибка "Phone must be between 11 and 21 characters." не должна присутствовать'

    def check_error_phone_wrong_format_present(self, should_be_present):
        is_present = self.is_element_present(*BasePageLocators.STUB_ERROR_MESSAGE)
        if should_be_present:
            assert is_present, \
                'Ошибка "must be a well-formed phone" отсутствует'
        else:
            assert not is_present, \
                'Ошибка "must be a well-formed phone" не должна присутствовать'

    def check_error_subject_is_blank_present(self, should_be_present):
        is_present = self.is_element_present(*MainPageLocators.ERROR_SUBJECT_IS_BLANK)
        if should_be_present:
            assert is_present, \
                'Ошибка "Subject may not be blank" отсутствует'
        else:
            assert not is_present, \
                'Ошибка "Subject may not be blank" не должна присутствовать'

    def check_error_subject_wrong_length_present(self, should_be_present):
        is_present = self.is_element_present(*MainPageLocators.ERROR_SUBJECT_WRONG_LENGTH)
        if should_be_present:
            assert is_present, \
                'Ошибка "Subject must be between 5 and 100 characters." отсутствует'
        else:
            assert not is_present, \
                'Ошибка "Subject must be between 5 and 100 characters." не должна присутствовать'

    def check_error_message_is_blank_present(self, should_be_present):
        is_present = self.is_element_present(*MainPageLocators.ERROR_MESSAGE_IS_BLANK)
        if should_be_present:
            assert is_present, \
                'Ошибка "Message may not be blank" отсутствует'
        else:
            assert not is_present, \
                'Ошибка "Message may not be blank" не должна присутствовать'

    def check_error_message_wrong_length_present(self, should_be_present):
        is_present = self.is_element_present(*MainPageLocators.ERROR_MESSAGE_WRONG_LENGTH)
        if should_be_present:
            assert is_present, \
                'Ошибка "Message must be between 20 and 2000 characters." отсутствует'
        else:
            assert not is_present, \
                'Ошибка "Message must be between 20 and 2000 characters." не должна присутствовать'

    def should_be_same_name_in_form(self, correct_name):
        got_name = self.get_text_from_element(*MainPageLocators.FILLED_FORM_NAME)
        assert got_name == f'Thanks for getting in touch {correct_name}!',\
            f'Имена отличаются: ожидалось {correct_name}, получено {got_name}'

    def should_be_same_subject_in_form(self, correct_subject):
        got_subject = self.get_text_from_element(*MainPageLocators.FILLED_FORM_SUBJECT)
        assert got_subject == correct_subject,\
            f'Темы отличаются: ожидалось {correct_subject}, получено {got_subject}'