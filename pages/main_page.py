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
        self._navigator = (By.CSS_SELECTOR, '#navigatorTree-body')
        self._navigator_elements = (By.CSS_SELECTOR, '.x-tree-node-text span')
        # Каталог "УЧЕТ ВЫПОЛНЕННЫХ РАБОТ" в навигаторе
        self._completed_work = (By.XPATH, '//tr[@data-qtip="УЧЕТ ВЫПОЛНЕННЫХ РАБОТ"]')
        # Режим "Ежедневный" на панели навигатора
        self._daily_mode = (By.XPATH, '//tr[@data-qtip="Ежедневный"]')
        # Открытая вкладка "Ежедневный" на рабочем столе
        self._tab_daily_mode = (By.XPATH, '//a[@role="tab"]//span[text()="Ежедневный"]')

    @property
    def navigator(self):
        return self._navigator

    @property
    def navigator_elements(self):
        return self._navigator_elements

    @property
    def tab_daily_mode(self):
        return self._tab_daily_mode

    def log_out(self):
        self.wait_visible(self._account).click()
        self.wait_visible(self._account_quit).click()
        self.wait_visible(self._button_accept).click()

    def collapse_navigator_directories(self):
        action = ActionChains(self.driver)
        navigator = self.wait_visible(self._navigator)
        action.context_click(navigator)
        action.move_by_offset(5, 5)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.RETURN)
        action.perform()

    def open_daily_mode(self):
        completed_work = self.find(self._completed_work)
        ActionChains(self.driver).double_click(completed_work).perform()
        daily_mode = self.find(self._daily_mode)
        ActionChains(self.driver).double_click(daily_mode).perform()
        self.wait_visible((By.XPATH, '//div[@class="x-grid-scroll-container "]'))
