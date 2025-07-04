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

    @allure.description('MP-2: Кнопка "Book Now" прокручивает страницу до раздела "Our Rooms"')
    def test_press_book_now_button(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        with allure.step('Нажимаем кнопку "Book Now"'):
            page.press_button_book_now()
        with allure.step('Результат: страница прокрутилась до раздела "Our Rooms"'):
            page.should_be_displayed_header_our_rooms()

    @allure.description('MP-3.1: Проверка доступности комнат, даты корректные')
    def test_set_correct_dates(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_header_check_dates()
        with allure.step('Нажимаем на кнопку "Check Availability"'):
            page.press_button_check_availability()
        with allure.step('Результат: свободные комнаты есть на корректные даты'):
            page.should_be_nth_room_card_displayed(cards_number=1)

    @allure.description('MP-3.2: Проверка доступности комнат, дата въезда позже даты выезда')
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

    @allure.description('MP-3.3: Проверка доступности дат, даты устаревшие')
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

    @allure.description('MP-4.1: Нажать "Submit" не заполняя форму')
    def test_press_submit_empty_send_us_a_message_form(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step('Нажимаем Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        with allure.step('Присутствует ошибка "Name may not be blank"'):
            page.check_error_name_is_blank_present(should_be_present=True)
        with allure.step('Присутствует ошибка "Email may not be blank"'):
            page.check_error_email_is_blank_present(should_be_present=True)
        with allure.step('Присутствует ошибка "Phone may not be blank"'):
            page.check_error_phone_is_blank_present(should_be_present=True)
        with allure.step('Присутствует ошибка "Phone must be between 11 and 21 characters."'):
            page.check_error_phone_wrong_length_present(should_be_present=True)
        with allure.step('Присутствует ошибка "Subject may not be blank"'):
            page.check_error_subject_is_blank_present(should_be_present=True)
        with allure.step('Присутствует ошибка "Subject must be between 5 and 100 characters."'):
            page.check_error_subject_wrong_length_present(should_be_present=True)
        with allure.step('Присутствует ошибка "Message may not be blank"'):
            page.check_error_message_is_blank_present(should_be_present=True)
        with allure.step('Присутствует ошибка "Message must be between 20 and 2000 characters."'):
            page.check_error_message_wrong_length_present(should_be_present=True)

    @allure.description('MP-4.2: Тесты поля Name')
    @pytest.mark.parametrize('name, expected_success',
                             [('Ivan', True),
                             ('Иван', True),
                             ('Ivan!', False),
                             ('Ivan1', False)]
                             )
    def test_name_field(self, open_main_page, name, expected_success):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step(f'Вставляем имя {name}'):
            page.input_name(name)
        with allure.step('Нажимаем Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        if expected_success:
            with allure.step('Результат: ошибки "Name may not be blank" и "must be a well-formed name" отсутствуют'):
                page.check_error_name_is_blank_present(should_be_present=False)
                page.check_error_name_wrong_format_present(should_be_present=False)
        else:
            with allure.step('Результат: ошибка "Name may not be blank" отсутствует, "must be a well-formed name" присутствует'):
                page.check_error_name_is_blank_present(should_be_present=False)
                page.check_error_name_wrong_format_present(should_be_present=True)

    @allure.description('MP-4.3: Тесты поля Email')
    @pytest.mark.parametrize('email, expected_success',
                             [('arseniy', False),
                              ('arseniym148@gmail', False),
                              ('arseniym148@gmail.com', True)])
    def test_email_field(self, open_main_page, email, expected_success):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step(f'Вставляем почту {email}'):
            page.input_email(email)
        with allure.step('Нажимаем Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        if expected_success:
            with allure.step('Результат: ошибки "Email may not be blank" и "must be a well-formed email address" отсутствуют'):
                page.check_error_email_is_blank_present(should_be_present=False)
                page.check_error_email_wrong_format_present(should_be_present=False)
        else:
            with allure.step('Результат: ошибка "Email may not be blank" отсутствует, "must be a well-formed email address" присутствует'):
                page.check_error_email_is_blank_present(should_be_present=False)
                page.check_error_email_wrong_format_present(should_be_present=True)

    @allure.description('MP-4.4: Тесты поля Phone')
    @pytest.mark.parametrize('phone, expected_wrong_format, expected_wrong_length',
                             [('aaaaa', True, False),
                              ('0123456789', False, True),
                              ('+0123456789', False, False),
                              ('012 345 67 89', False, False),
                              ('012 345-67-89', False, False),
                              ('(012) 345-67-89', False, False),
                              ('01234567890', False, False),
                              ('0'*21, False, False),
                              ('0'*22, False, True),
                             ])
    def test_phone_field(self, open_main_page, phone, expected_wrong_format, expected_wrong_length):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step(f'Вставляем номер телефона {phone}'):
            page.input_phone(phone)
        with allure.step('Нажимаем Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        if expected_wrong_format:
            with allure.step('Результат: ошибки "Phone may not be blank"'
                             'и "Phone must be between 11 and 21 characters." отсутствует'
                             ', ошибка "must be a well-formed email address" присутствует'):
                page.check_error_phone_wrong_format_present(should_be_present=True)
                page.check_error_phone_is_blank_present(should_be_present=False)
                page.check_error_phone_wrong_length_present(should_be_present=False)
        elif expected_wrong_length:
            with allure.step('Результат: ошибки "must be a well-formed phone"'
                             'и "Phone may not be blank" отсутствует'
                             ', ошибка "Phone must be between 11 and 21 characters." присутствует'):
                page.check_error_phone_wrong_format_present(should_be_present=False)
                page.check_error_phone_is_blank_present(should_be_present=False)
                page.check_error_phone_wrong_length_present(should_be_present=True)
        else:
            with allure.step('Результат: ошибки "must be a well-formed phone"'
                             'и "Phone may not be blank" отсутствует'
                             ', "Phone must be between 11 and 21 characters." отсутствует'):
                page.check_error_phone_wrong_format_present(should_be_present=False)
                page.check_error_phone_is_blank_present(should_be_present=False)
                page.check_error_phone_wrong_length_present(should_be_present=False)

    @allure.description('MP-4.5: Тесты поля Subject')
    @pytest.mark.parametrize('subject, expected_success',
                             [('abcd', False),
                              ('abcde', True),
                              ('a'*100, True),
                              ('a'*101, False)])
    def test_subject_field(self, open_main_page, subject, expected_success):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step(f'Вставляем тему письма {subject}'):
            page.input_subject(subject)
        with allure.step('Нажимаем Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        if expected_success:
            with allure.step(
                    'Результат: ошибки "Subject may not be blank" и "Subject must be between 5 and 100 characters." отсутствуют'):
                page.check_error_subject_is_blank_present(should_be_present=False)
                page.check_error_subject_wrong_length_present(should_be_present=False)
        else:
            with allure.step(
                    'Результат: ошибка "Subject may not be blank" отсутствует, "Subject must be between 5 and 100 characters." присутствует'):
                page.check_error_subject_is_blank_present(should_be_present=False)
                page.check_error_subject_wrong_length_present(should_be_present=True)


    @allure.description('MP-4.6: Тесты поля Message')
    @pytest.mark.parametrize('message, expected_success',
                                 [('a'*19, False),
                                  ('a'*20, True),
                                  ('a'*2000, True),
                                  ('a'*2001, False)])
    def test_message_field(self, open_main_page, message, expected_success):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step(f'Вставляем тему письма {message}'):
            page.input_message(message)
        with allure.step('Нажимаем Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        if expected_success:
            with allure.step(
                    'Результат: ошибки "Message may not be blank" и "Message must be between 20 and 2000 characters." отсутствуют'):
                page.check_error_message_is_blank_present(should_be_present=False)
                page.check_error_message_wrong_length_present(should_be_present=False)
        else:
            with allure.step(
                    'Результат: ошибка "Message may not be blank" отсутствует, "Message must be between 20 and 2000 characters." присутствует'):
                page.check_error_message_is_blank_present(should_be_present=False)
                page.check_error_message_wrong_length_present(should_be_present=True)


    @allure.description('MP-4.7: Все поля заполнены корректно')
    def test_form_filled_correctly(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        data = {'name': 'Arseniy', 'email': 'arseniym148@gmail.com', 'phone': '+1234567890',
                'subject': 'Booking', 'message': 'I can\'t book a room on the website'}
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step('Вставляем корректные данные в форму'):
            page.input_name(data['name'])
            page.input_email(data['email'])
            page.input_phone(data['phone'])
            page.input_subject(data['subject'])
            page.input_message(data['message'])
        with allure.step('Нажимаем Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        with allure.step('Появилось уведомление об успешной отправке сообщения, корректно указаны имя и тема сообщения'):
            page.should_be_same_name_in_form(correct_name=data['name'])
            page.should_be_same_subject_in_form(correct_subject=data['subject'])
            page.take_screenshot()