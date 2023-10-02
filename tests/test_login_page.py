import os

from dotenv import load_dotenv

from pages.login_page import LoginPage

load_dotenv()
URL = os.getenv('URL')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


class TestLoginPage:
    def test_login(self, driver):
        login_page = LoginPage(driver, URL)
        login_page.open()
        login_page.close_error_window()
