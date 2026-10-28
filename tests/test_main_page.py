import pytest
import allure
from pages.main_page import MainPage

@allure.description('Main page tests')

class TestMainPage():
    @allure.description('MP-1: Main page is opened')
    def test_opened_main_page(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        with allure.step('Result: the main page should be opened'):
            page.should_be_opened_main_page()

    @allure.description('MP-2: The "Book Now" button scrolls the page to the "Our Rooms" section')
    def test_press_book_now_button(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        with allure.step('Click the "Book Now" button'):
            page.press_button_book_now()
        with allure.step('Result: the page scrolled to the "Our Rooms" section'):
            page.should_be_displayed_header_our_rooms()

    @allure.description('MP-3.1: Check room availability with valid dates')
    def test_set_correct_dates(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_header_check_dates()
        with allure.step('Click the "Check Availability" button'):
            page.press_button_check_availability()
        with allure.step('Result: available rooms are shown for valid dates'):
            page.should_be_nth_room_card_displayed(cards_number=1)

    @allure.description('MP-3.2: Check room availability when the check-in date is later than the check-out date')
    @pytest.mark.xfail(reason='An error is expected when the check-in date is later than the check-out date, but it is missing')
    def test_set_check_in_date_later_than_check_out(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_header_check_dates()
        with allure.step('Set Check In to the 15th day of the next month'):
            page.set_calendar_date(date_type='check in', months_offset=1, day=15)
        with allure.step('Set Check Out to the 10th day of the next month'):
            page.set_calendar_date(date_type='check out', months_offset=1, day=10)
        with allure.step('Click the "Check Availability" button'):
            page.press_button_check_availability()
        with allure.step('Result: a date error message is shown'):
            page.should_be_stub_error_message()

    @allure.description('MP-3.3: Check room availability with past dates')
    @pytest.mark.xfail(reason='An error is expected when past dates are selected, but it is missing')
    def test_set_past_dates(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_header_check_dates()
        with allure.step('Set Check In to the 1st day of the previous month'):
            page.set_calendar_date(date_type='check in', months_offset=-1, day=1)
        with allure.step('Set Check Out to the 3rd day of the previous month'):
            page.set_calendar_date(date_type='check out', months_offset=-1, day=3)
        with allure.step('Click the "Check Availability" button'):
            page.press_button_check_availability()
        with allure.step('Result: a date error message is shown'):
            page.should_be_stub_error_message()

    @allure.description('MP-4.1: Click "Submit" without filling out the form')
    def test_press_submit_empty_send_us_a_message_form(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step('Click Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        with allure.step('The "Name may not be blank" error is shown'):
            page.check_error_name_is_blank_present(should_be_present=True)
        with allure.step('The "Email may not be blank" error is shown'):
            page.check_error_email_is_blank_present(should_be_present=True)
        with allure.step('The "Phone may not be blank" error is shown'):
            page.check_error_phone_is_blank_present(should_be_present=True)
        with allure.step('The "Phone must be between 11 and 21 characters." error is shown'):
            page.check_error_phone_wrong_length_present(should_be_present=True)
        with allure.step('The "Subject may not be blank" error is shown'):
            page.check_error_subject_is_blank_present(should_be_present=True)
        with allure.step('The "Subject must be between 5 and 100 characters." error is shown'):
            page.check_error_subject_wrong_length_present(should_be_present=True)
        with allure.step('The "Message may not be blank" error is shown'):
            page.check_error_message_is_blank_present(should_be_present=True)
        with allure.step('The "Message must be between 20 and 2000 characters." error is shown'):
            page.check_error_message_wrong_length_present(should_be_present=True)

    @allure.description('MP-4.2: Name field tests')
    @pytest.mark.parametrize('name',
                             [('Ivan'),
                             ('John'),
                             ('Ivan!'),
                             ('Ivan1')]
                             )
    def test_name_field(self, open_main_page, name):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step(f'Enter name {name}'):
            page.input_name(name)
        with allure.step('Click Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        with allure.step('Result: the "Name may not be blank" error is not shown'):
            page.check_error_name_is_blank_present(should_be_present=False)

    @allure.description('MP-4.3: Email field tests')
    @pytest.mark.parametrize('email, expected_success',
                             [('arseniy', False),
                              ('arseniym148@gmail', True),
                              ('arseniym148@gmail.com', True)])
    def test_email_field(self, open_main_page, email, expected_success):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step(f'Enter email {email}'):
            page.input_email(email)
        with allure.step('Click Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        if expected_success:
            with allure.step(
                    'Result: the "Email may not be blank" and "must be a well-formed email address" errors are not shown'):
                page.check_error_email_is_blank_present(should_be_present=False)
                page.check_error_email_wrong_format_present(should_be_present=False)
        else:
            with allure.step(
                    'Result: the "Email may not be blank" error is not shown, and the "must be a well-formed email address" error is shown'):
                page.check_error_email_is_blank_present(should_be_present=False)
                page.check_error_email_wrong_format_present(should_be_present=True)

    @allure.description('MP-4.4: Phone field tests')
    @pytest.mark.parametrize('phone, expected_wrong_length',
                             [('aaaaa', True),
                              ('0123456789', True),
                              ('+0123456789', False),
                              ('012 345 67 89', False),
                              ('012 345-67-89', False),
                              ('(012) 345-67-89', False),
                              ('01234567890', False),
                              ('0'*21, False),
                              ('0'*22, True),
                             ])
    def test_phone_field(self, open_main_page, phone, expected_wrong_length):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step(f'Enter phone number {phone}'):
            page.input_phone(phone)
        with allure.step('Click Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        if expected_wrong_length:
            with allure.step('Result: "Phone may not be blank" error is not shown, '
                             'and the "Phone must be between 11 and 21 characters." error is shown'):
                page.check_error_phone_is_blank_present(should_be_present=False)
                page.check_error_phone_wrong_length_present(should_be_present=True)
        else:
            with allure.step('Result: "Phone may not be blank", '
                             'and the "Phone must be between 11 and 21 characters." errors are not shown'):
                page.check_error_phone_is_blank_present(should_be_present=False)
                page.check_error_phone_wrong_length_present(should_be_present=False)

    @allure.description('MP-4.5: Subject field tests')
    @pytest.mark.parametrize('subject, expected_success',
                             [('abcd', False),
                              ('abcde', True),
                              ('a'*100, True),
                              ('a'*101, False)])
    def test_subject_field(self, open_main_page, subject, expected_success):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step(f'Enter subject {subject}'):
            page.input_subject(subject)
        with allure.step('Click Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        if expected_success:
            with allure.step(
                    'Result: the "Subject may not be blank" and "Subject must be between 5 and 100 characters." errors are not shown'):
                page.check_error_subject_is_blank_present(should_be_present=False)
                page.check_error_subject_wrong_length_present(should_be_present=False)
        else:
            with allure.step(
                    'Result: the "Subject may not be blank" error is not shown, and the "Subject must be between 5 and 100 characters." error is shown'):
                page.check_error_subject_is_blank_present(should_be_present=False)
                page.check_error_subject_wrong_length_present(should_be_present=True)


    @allure.description('MP-4.6: Message field tests')
    @pytest.mark.parametrize('message, expected_success',
                                 [('a'*19, False),
                                  ('a'*20, True),
                                  ('a'*2000, True),
                                  ('a'*2001, False)])
    def test_message_field(self, open_main_page, message, expected_success):
        browser, link = open_main_page
        page = MainPage(browser, link)
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step(f'Enter message {message}'):
            page.input_message(message)
        with allure.step('Click Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        if expected_success:
            with allure.step(
                    'Result: the "Message may not be blank" and "Message must be between 20 and 2000 characters." errors are not shown'):
                page.check_error_message_is_blank_present(should_be_present=False)
                page.check_error_message_wrong_length_present(should_be_present=False)
        else:
            with allure.step(
                    'Result: the "Message may not be blank" error is not shown, and the "Message must be between 20 and 2000 characters." error is shown'):
                page.check_error_message_is_blank_present(should_be_present=False)
                page.check_error_message_wrong_length_present(should_be_present=True)


    @allure.description('MP-4.7: All fields are filled correctly')
    def test_form_filled_correctly(self, open_main_page):
        browser, link = open_main_page
        page = MainPage(browser, link)
        data = {'name': 'Arseniy', 'email': 'arseniym148@gmail.com', 'phone': '+1234567890',
                'subject': 'Booking', 'message': 'I can\'t book a room on the website'}
        page.scroll_to_submit_send_us_a_message_form()
        with allure.step('Enter valid data into the form'):
            page.input_name(data['name'])
            page.input_email(data['email'])
            page.input_phone(data['phone'])
            page.input_subject(data['subject'])
            page.input_message(data['message'])
        with allure.step('Click Submit'):
            page.press_submit_send_us_a_message_form()
        page.take_screenshot()
        with allure.step('A success notification is shown, and the name and subject are displayed correctly'):
            page.should_be_same_name_in_form(correct_name=data['name'])
            page.should_be_same_subject_in_form(correct_subject=data['subject'])
            page.take_screenshot()
