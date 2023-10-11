import allure
import pytest

from pages.login_page import LoginPage
from test_data import LOGIN, PASSWORD


@allure.suite('LoginPage')
class TestLoginPage:

    @allure.title('Проверка ввода верных учетных данных (логина и пароля)')
    def test_login_page_right_credentials(self, driver):
        login_page = LoginPage(driver)
        main_page = login_page.main_page

        # Открытие страницы логирования
        login_page.open()

        # Проверка загрузки страницы логирования
        assert login_page.login.is_displayed(), 'Отсутствует поле ввода логина.'
        assert login_page.password.is_displayed(), 'Отсутствует поле ввода пароля.'

        # Заполнение учетных данных
        login_page.fill_login(LOGIN)
        login_page.fill_password(PASSWORD)
        login_page.submit()

        # Проверка, что панель навигатора доступна
        assert main_page.navigator.is_enabled()

        main_page.log_out()

    @allure.title('Проверка ввода НЕВЕРНЫХ учетных данных (логина и пароля)')
    @pytest.mark.parametrize('login, password', [
        (LOGIN, '3'),
        ('wrong_login', PASSWORD),
        ('wrong_login', 'wrong_password')
    ])
    def test_login_page_wrong_credentials(self, login, password, driver):
        login_page = LoginPage(driver)

        # Открытие страницы логирования
        login_page.open()

        # Заполнение учетных данных
        login_page.fill_login(login)
        login_page.fill_password(password)
        login_page.submit()

        # Проверка появления сообщения о неверных учетных данных
        assert login_page.warning.text == 'Неверное имя пользователя или пароль.'


