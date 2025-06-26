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

    def get_select_of_nth_room_card(n):
        return (By.XPATH, f'(//div[@class="col-md-6 col-lg-4"])[{n}]')
    def get_select_nth_date_in_current_month_calendar(current_month, n):
        return (By.XPATH, f'//div[contains(@class, "react-datepicker__day") and contains(@aria-label, "{current_month}") and text()="{n}"]')