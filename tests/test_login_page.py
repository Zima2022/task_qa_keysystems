import allure
import pytest

from pages.login_page import LoginPage
from test_data import DIRECTORIES, LOGIN, PASSWORD


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

    @allure.title('Проверка загрузки панели навигатора')
    def test_navigator(self, driver):
        login_page = LoginPage(driver)
        main_page = login_page.main_page

        # Открытие страницы логирования
        login_page.open()

        # Прохождение аутентификации
        login_page.auth(LOGIN, PASSWORD)

        # Сворачиваем все директории в панели навигатора
        main_page.collapse_navigator_directories()

        # Проверка наличия обязательных директорий в панели навигатора
        actual_directories = [item.text for item in main_page.navigator_elements]
        assert all(directory in actual_directories for directory in DIRECTORIES)

        main_page.log_out()

    @allure.title('Проверка открытия режима "Ежедневный" из навигатора')
    def test_open_daily_mode(self, driver):
        login_page = LoginPage(driver)
        main_page = login_page.main_page

        # Открытие страницы логирования
        login_page.open()

        # Прохождение аутентификации
        login_page.auth(LOGIN, PASSWORD)

        # Отрытие режима "Ежедневный"
        main_page.open_daily_mode()

        # Проверка загрузки режима "Ежедневный"
        assert main_page.tab_daily_mode.text == 'Ежедневный'
        assert main_page.tab_daily_mode.is_displayed()

        main_page.log_out()
