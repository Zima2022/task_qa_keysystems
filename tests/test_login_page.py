import os

from dotenv import load_dotenv

from locators.login_page_locators import LoginPageLocators
from pages.login_page import LoginPage

load_dotenv()
URL = os.getenv('URL')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


class TestLoginPage:
    def test_login_page_has_fields_login_and_password(self, driver):
        login_page = LoginPage(driver, URL)
        login_page.open()
        login_page.close_error_window()
        assert login_page.is_element_present(LoginPageLocators.LOGIN), 'Отсутствует поле ввода логина'
        assert login_page.is_element_present(LoginPageLocators.PASSWORD), 'Отсутствует поле ввода пароля'
