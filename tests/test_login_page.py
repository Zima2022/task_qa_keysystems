import os

import allure
import pytest

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
        assert login_page.is_element_visible(login_page.login), 'Отсутствует поле ввода логина'
        assert login_page.is_element_visible(login_page.password), 'Отсутствует поле ввода пароля'
        login_page.fill_login(LOGIN)
        login_page.fill_password(PASSWORD)
        login_page.submit()
        main_page = login_page.main_page
        assert main_page.find(main_page.navigator).is_enabled()
        main_page.log_out()

    @allure.title('Проверка ввода НЕВЕРНЫХ учетных данных (логина и пароля)')
    @pytest.mark.parametrize('login, password', [
        (LOGIN, '3'),
        # ('wrong_login', PASSWORD),
        # ('wrong_login', 'wrong_password')
    ])
    def test_login_page_wrong_credentials(self, login, password, driver):
        driver.implicitly_wait(5)
        login_page = LoginPage(driver)
        login_page.open()
        login_page.fill_login(login)
        login_page.fill_password(password)
        login_page.submit()
        assert login_page.find(login_page.warning).text == 'Неверное имя пользователя или пароль.'

    @allure.title('Проверка загрузки панели навигатора')
    def test_navigator(self, driver):
        driver.implicitly_wait(5)
        login_page = LoginPage(driver)
        login_page.open()
        login_page.auth(LOGIN, PASSWORD)
        main_page = login_page.main_page
        main_page.collapse_navigator_directories()
        navigator_directories = main_page.find_elements(main_page.navigator_elements)
        directories = ('УЧЕТ ВЫПОЛНЕННЫХ РАБОТ', 'БАГ-ТРЕКИНГ', 'ОТЧЕТЫ', 'СПРАВОЧНИКИ')
        actual_directories = [item.text for item in navigator_directories]
        assert all(directory in actual_directories for directory in directories)
        main_page.log_out()

    @allure.title('Проверка открытия режима "Ежедневный" из навигатора')
    def test_open_daily_mode(self, driver):
        # driver.implicitly_wait(10)
        login_page = LoginPage(driver)
        login_page.open()
        login_page.wait_visible(login_page.login)
        login_page.auth(LOGIN, PASSWORD)
        main_page = login_page.main_page
        main_page.open_daily_mode()
        assert main_page.wait_visible(main_page.tab_daily_mode).text == 'Ежедневный'
        assert main_page.is_element_visible(main_page.tab_daily_mode)
        main_page.log_out()
