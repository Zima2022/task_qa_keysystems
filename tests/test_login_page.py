import os

import pytest

from locators.main_page_locators import MainPageLocators
from pages.login_page import LoginPage

URL = os.getenv('URL')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


class TestLoginPage:
    def test_login_page_right_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.wait_for_error_window()
        login_page._client_error_window.close()
        assert login_page.is_element_visible(login_page._login), 'Отсутствует поле ввода логина'
        assert login_page.is_element_visible(login_page._password), 'Отсутствует поле ввода пароля'
        login_page.fill_login(LOGIN)
        login_page.fill_password(PASSWORD)
        login_page.submit()
        assert login_page.wait_visible(MainPageLocators.NAVIGATOR).is_enabled()

    @pytest.mark.parametrize('login, password', [
        (LOGIN, '3'),
        ('wrong_login', PASSWORD),
        ('wrong_login', 'wrong_password')
    ])
    def test_login_page_wrong_credentials(self, login, password, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.wait_for_error_window()
        login_page._client_error_window.close()
        login_page.fill_login(login)
        login_page.fill_password(password)
        login_page.submit()
        login_page.wait_visible(login_page._warning)
        assert login_page.find(login_page._warning).text == 'Неверное имя пользователя или пароль.'
