import os

from dotenv import load_dotenv
from selenium.common import NoSuchElementException

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
        try:
            login_page.find(LoginPageLocators.LOGIN)
        except NoSuchElementException:
            assert False, 'Отсутствует поле для ввода логина'

        try:
            login_page.find(LoginPageLocators.PASSWORD)
        except NoSuchElementException:
            assert False, 'Отсутствует поле для ввода пароля'
