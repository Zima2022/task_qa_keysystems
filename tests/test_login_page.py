import os

import pytest
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait

from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
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
        login_page.fill_login(LOGIN)
        login_page.fill_password(PASSWORD)
        login_page.submit()
        login_page.wait_visible(MainPageLocators.BUTTON_OK, 10).click()
        assert login_page.wait_visible(MainPageLocators.NAVIGATOR).is_displayed()

    @pytest.mark.parametrize('login,password', [(LOGIN, '3')])
    def test_login_page_wrong_credentials(self, login, password, driver):
        login_page = LoginPage(driver, URL)
        login_page.open()
        login_page.close_error_window()
        login_page.fill_login(login)
        login_page.fill_password(password)
        login_page.submit()
        login_page.wait_visible(LoginPageLocators.WARNING)
        assert login_page.find(LoginPageLocators.WARNING).text == 'Неверное имя пользователя или пароль.'
