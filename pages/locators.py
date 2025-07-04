from selenium.webdriver.common.by import By

class BasePageLocators():
    '''
    Заглушка, для случаев когда должна появиться ошибка, но она не появляется, а сослаться на ошибку надо
    '''
    STUB_ERROR_MESSAGE = (By.CLASS_NAME, 'error-message')
class MainPageLocators():
    WELCOME_MESSAGE = (By.CLASS_NAME, 'display-4')
    HEADER_OUR_ROOMS = (By.XPATH, '//h2[text()="Our Rooms"]')
    HEADER_CHECK_DATES = (By.CSS_SELECTOR, '.card-title.text-center.mb-4')
    BUTTON_BOOK_NOW = (By.CSS_SELECTOR, '.btn.btn-primary.btn-lg')
    CHECK_IN_DATE = (By.XPATH, '(//div[@class="react-datepicker__input-container"])[1]')
    CHECK_OUT_DATE = (By.XPATH, '(//div[@class="react-datepicker__input-container"])[2]')
    BUTTON_CHECK_AVAILABILITY = (By.CSS_SELECTOR, '.col-8.mt-4 > button')
    BUTTON_NEXT_MONTH = (By.XPATH, '//button[@aria-label="Next Month"]')
    BUTTON_PREVIOUS_MONTH = (By.XPATH, '//button[@aria-label="Previous Month"]')
    CURRENT_DATE_CALENDAR = (By.CLASS_NAME, 'react-datepicker__current-month')
    HEADER_SEND_US_A_MESSAGE = (By.CSS_SELECTOR, '.h4.mb-4.text-center')
    FILLED_FORM_NAME = (By.CSS_SELECTOR, '.card-body.p-4 > .h4.mb-4')
    FILLED_FORM_SUBJECT = (By.XPATH, '//div[@class="card-body p-4"]//p[@style="font-weight: bold;"]')

    def get_select_of_nth_room_card(n):
        return (By.XPATH, f'(//div[@class="col-md-6 col-lg-4"])[{n}]')
    def get_select_nth_date_in_current_month_calendar(current_month, n):
        return (By.XPATH, f'//div[contains(@class, "react-datepicker__day") and contains(@aria-label, "{current_month}") and text()="{n}"]')

    # Форма Send Us a Message
    INPUT_NAME = (By.ID, 'name')
    INPUT_EMAIL = (By.ID, 'email')
    INPUT_PHONE = (By.ID, 'phone')
    INPUT_SUBJECT = (By.ID, 'subject')
    INPUT_MESSAGE = (By.ID, 'description')
    SUBMIT_SEND_US_A_MESSAGE_FORM = (By.CSS_SELECTOR, '.d-grid > button')

    # Ошибки формы Send Us a Message
    ERRORS_SEND_US_A_MESSAGE_FORM = (By.CLASS_NAME, 'alert alert-danger')
    ERROR_NAME_IS_BLANK = (By.XPATH, '//div[@class="alert alert-danger"]//p[text()="Name may not be blank"]')
    ERROR_EMAIL_IS_BLANK = (By.XPATH, '//div[@class="alert alert-danger"]//p[text()="Email may not be blank"]')
    ERROR_EMAIL_WRONG_FORM = (By.XPATH, '//div[@class="alert alert-danger"]//p[text()="must be a well-formed email address"]')
    ERROR_PHONE_IS_BLANK = (By.XPATH, '//div[@class="alert alert-danger"]//p[text()="Phone may not be blank"]')
    ERROR_PHONE_WRONG_LENGTH = (By.XPATH, '//div[@class="alert alert-danger"]//p[text()="Phone must be between 11 and 21 characters."]')
    ERROR_SUBJECT_IS_BLANK = (By.XPATH, '//div[@class="alert alert-danger"]//p[text()="Subject may not be blank"]')
    ERROR_SUBJECT_WRONG_LENGTH = (By.XPATH, '//div[@class="alert alert-danger"]//p[text()="Subject must be between 5 and 100 characters."]')
    ERROR_MESSAGE_IS_BLANK = (By.XPATH, '//div[@class="alert alert-danger"]//p[text()="Message may not be blank"]')
    ERROR_MESSAGE_WRONG_LENGTH = (By.XPATH, '//div[@class="alert alert-danger"]//p[text()="Message must be between 20 and 2000 characters."]')