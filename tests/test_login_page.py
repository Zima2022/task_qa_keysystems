import os

import allure
import pytest

from locators.main_page_locators import MainPageLocators
from pages.login_page import LoginPage

URL = os.getenv('URL')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


@allure.suite('LoginPage')
class TestLoginPage:
    @allure.title('Проверка ввода верных учетных данных (логина и пароля)')
    def test_login_page_right_credentials(self, driver):
        driver.implicitly_wait(5)
        login_page = LoginPage(driver)
        login_page.open()
        # login_page.error_window.close()
        assert login_page.is_element_visible(login_page._login), 'Отсутствует поле ввода логина'
        assert login_page.is_element_visible(login_page._password), 'Отсутствует поле ввода пароля'
        login_page.fill_login(LOGIN)
        login_page.fill_password(PASSWORD)
        login_page.submit()
        assert login_page.find(MainPageLocators.NAVIGATOR).is_enabled()
        login_page.log_out()

    @allure.title('Проверка ввода НЕВЕРНЫХ учетных данных (логина и пароля)')
    @pytest.mark.parametrize('login, password', [
        (LOGIN, '3'),
        ('wrong_login', PASSWORD),
        ('wrong_login', 'wrong_password')
    ])
    def test_login_page_wrong_credentials(self, login, password, driver):
        driver.implicitly_wait(5)
        login_page = LoginPage(driver)
        login_page.open()
        login_page.error_window.close()
        login_page.fill_login(login)
        login_page.fill_password(password)
        login_page.submit()
        # login_page.wait_visible(login_page._warning)
        assert login_page.find(login_page._warning).text == 'Неверное имя пользователя или пароль.'

    @allure.title('Проверка загрузки панели навигатора')
    def test_navigator(self, driver):
        driver.implicitly_wait(5)
        login_page = LoginPage(driver)
        login_page.open()
        login_page.auth(LOGIN, PASSWORD)
        login_page.collapse_navigator_directories()
        navigator_directories = login_page.find_elements(MainPageLocators.NAVIGATOR_ELEMENTS)
        directories = ('УЧЕТ ВЫПОЛНЕННЫХ РАБОТ', 'БАГ-ТРЕКИНГ', 'ОТЧЕТЫ', 'СПРАВОЧНИКИ')
        actual_directories = [item.text for item in navigator_directories]
        assert all(directory in actual_directories for directory in directories)
        login_page.log_out()

    @allure.title('Проверка открытия режима "Ежедневный" из навигатора')
    def test_open_daily_mode(self, driver):
        driver.implicitly_wait(10)
        login_page = LoginPage(driver)
        login_page.open()
        login_page.auth(LOGIN, PASSWORD)
        login_page.open_daily_mode()
        assert login_page.find(MainPageLocators.TAB_DAILY_MODE).text == 'Ежедневный'
        assert login_page.is_element_visible(MainPageLocators.TAB_DAILY_MODE)
        login_page.log_out()
