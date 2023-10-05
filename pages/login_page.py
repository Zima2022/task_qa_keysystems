from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.error_window_page import ErrorWindowPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._client_error_window = ErrorWindowPage(driver)
        self._login = (By.CSS_SELECTOR, '#textfield-1018-inputEl')
        self._password = (By.CSS_SELECTOR, '#textfield-1019-inputEl')
        self._login_button = (By.CSS_SELECTOR, '#button-1022-btnInnerEl')
        self._error_window_locator = (By.CSS_SELECTOR, '#ks-clienterror-window-1050')
        self._warning = (By.CSS_SELECTOR, '#box-1065')

    @property
    def error_window(self):
        return self._client_error_window

    def wait_for_error_window(self):
        self.wait_visible(self._error_window_locator)

    def fill_login(self, login):
        self.find(self._login).send_keys(login)

    def fill_password(self, password):
        self.find(self._password).send_keys(password)

    def submit(self):
        self.find(self._login_button).click()
