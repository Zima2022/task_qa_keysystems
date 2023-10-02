from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def close_error_window(self):
        """Закрывает окно, которое появляется при стартовой загрузке
        и мешает ввести логин и пароль."""
        button = self.element_is_visible(LoginPageLocators.BUTTON_CLOSE, 5)
        button.click()
