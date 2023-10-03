from selenium.common import TimeoutException

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def close_error_window(self):
        """Закрывает окно, которое появляется при стартовой загрузке
        и мешает ввести логин и пароль."""
        try:
            button = self.wait_visible(LoginPageLocators.BUTTON_CLOSE, 5)
            button.click()
        except TimeoutException:
            pass

    def fill_login(self, login):
        self.find(LoginPageLocators.LOGIN).send_keys(login)

    def fill_password(self, password):
        self.find(LoginPageLocators.PASSWORD).send_keys(password)

    def submit(self):
        self.find(LoginPageLocators.LOGIN_BUTTON).click()
