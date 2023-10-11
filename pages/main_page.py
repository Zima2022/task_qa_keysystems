from time import sleep

import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Аккаунт, под которы пользователь авторизован в приложении
        self._account = (By.CSS_SELECTOR, '#ks-core-dashboard-header-useraccountbtn-1114-btnInnerEl')
        # Меню "Выйти" из аккаунта
        self._account_quit = (By.XPATH, '//span[text()="Выйти"]')
        # Кнопка ОК диалогового окна для подтверждения выхода из аккаунта
        self._button_accept = (By.XPATH, '//div[@role="dialog"]//a[1]')
        # Панель навигатора
        self._navigator = (By.CSS_SELECTOR, '#navigatorTree-body')
        # Содержимое панели навигатора
        self._navigator_elements = (By.CSS_SELECTOR, '.x-tree-node-text span')
        # Каталог "УЧЕТ ВЫПОЛНЕННЫХ РАБОТ" в навигаторе
        self._completed_work = (By.XPATH, '//tr[@data-qtip="УЧЕТ ВЫПОЛНЕННЫХ РАБОТ"]')
        # Режим "Ежедневный" на панели навигатора
        self._daily_mode = (By.XPATH, '//tr[@data-qtip="Ежедневный"]')
        # Открытая вкладка "Ежедневный" на рабочем столе
        self._tab_daily_mode = (By.XPATH, '//a[@role="tab"]//span[text()="Ежедневный"]')
        # Контент вкладки "Ежедневный"
        self._content_daily_mode = (By.XPATH, '//div[@class="x-grid-scroll-container "]')

    @property
    def navigator(self):
        return self.wait_visible(self._navigator)

    @property
    def navigator_elements(self):
        return self.find_elements(self._navigator_elements)

    @property
    def account(self):
        return self.wait_visible(self._account)

    @property
    def account_quit(self):
        return self.wait_clickable(self._account_quit)

    @property
    def button_accept(self):
        return self.wait_visible(self._button_accept)

    @property
    def completed_work(self):
        return self.wait_visible(self._completed_work)

    @property
    def daily_mode(self):
        return self.find(self._daily_mode)

    @property
    def content_daily_mode(self):
        return self.wait_visible(self._content_daily_mode)

    @property
    def tab_daily_mode(self):
        return self.wait_visible(self._tab_daily_mode)

    @allure.step('Завершаем сессию')
    def log_out(self):
        self.account.click()
        self.account_quit.click()
        self.button_accept.click()

    @allure.step('Сворачиваем все каталоги в панели навигатора')
    def collapse_navigator_directories(self):
        navigator = self.navigator
        action = ActionChains(self.driver)
        action.context_click(navigator)
        action.move_by_offset(5, 5)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.RETURN)
        action.perform()

    @allure.step('Открываем режим "Ежедневный"')
    def open_daily_mode(self):
        with allure.step('Двойной клик по директории "УЧЕТ ВЫПОЛНЕННЫХ РАБОТ" в панели навигатора'):
            ActionChains(self.driver).double_click(self.completed_work).perform()
        with allure.step('Двойной клик "Ежедневный" в панели навигатора'):
            ActionChains(self.driver).double_click(self.daily_mode).perform()
        with allure.step('Ожидаем загрузки содержимого вкладки "Ежедневный"'):
            assert self.content_daily_mode.is_displayed()
        sleep(1)
