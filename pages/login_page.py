import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.error_window_page import ErrorWindowPage
from pages.main_page import MainPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._client_error_window = ErrorWindowPage(driver)
        self._main_page = MainPage(driver)
        # Поле ввода логина
        self._login = (By.CSS_SELECTOR, '#textfield-1018-inputEl')
        # Поле ввода пароля
        self._password = (By.CSS_SELECTOR, '#textfield-1019-inputEl')
        # Кнопка "Войти"
        self._login_button = (By.CSS_SELECTOR, '#button-1022-btnInnerEl')
        self._error_window_locator = (By.CSS_SELECTOR, '#ks-clienterror-window-1050')
        # Всплывающее окно, которое появляется при вводе неверных учетных данных
        self._warning = (
            By.XPATH,
            '//div[@class="x-component ks-core-messagebox__message x-box-item x-component-default"]'
        )

    @property
    def error_window(self):
        return self._client_error_window

    @property
    def login(self):
        return self.wait_visible(self._login)

    @property
    def password(self):
        return self.find(self._password)

    @property
    def main_page(self):
        return self._main_page

    @property
    def login_button(self):
        return self.find(self._login_button)

    @property
    def warning(self):
        return self.wait_visible(self._warning)

    @allure.step('Заполняем поле логин юзера {login}')
    def fill_login(self, login):
        self.login.send_keys(login)

    @allure.step('Заполняем поле пароль')
    def fill_password(self, password):
        self.password.send_keys(password)

    @allure.step('Нажимаем кнопку Войти')
    def submit(self):
        self.login_button.click()

    @allure.step('Проходим аутентификацию для юзера {login}')
    def auth(self, login, password):
        self.fill_login(login)
        self.fill_password(password)
        self.submit()
