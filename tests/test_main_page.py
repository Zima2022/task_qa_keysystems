import allure

from pages.login_page import LoginPage
from test_data import DIRECTORIES, LOGIN, PASSWORD


@allure.suite('MainPage')
class TestMainPage:

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
