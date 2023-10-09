import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.error_window_page import ErrorWindowPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._client_error_window = ErrorWindowPage(driver)
        self._login = (By.CSS_SELECTOR, '#textfield-1018-inputEl')
        self._password = (By.CSS_SELECTOR, '#textfield-1019-inputEl')
        self._login_button = (By.CSS_SELECTOR, '#button-1022-btnInnerEl')
        self._error_window_locator = (By.CSS_SELECTOR, '#ks-clienterror-window-1050')
        self._warning = (
            By.XPATH,
            '//div[@class="x-component ks-core-messagebox__message x-box-item x-component-default"]'
        )

    @property
    def error_window(self):
        return self._client_error_window

    def fill_login(self, login):
        self.find(self._login).send_keys(login)

    def fill_password(self, password):
        self.find(self._password).send_keys(password)

    def submit(self):
        self.find(self._login_button).click()

    def auth(self, login, password):
        # self.error_window.close()
        self.fill_login(login)
        self.fill_password(password)
        self.submit()

    def log_out(self):
        self.wait_visible(MainPageLocators.ACCOUNT).click()
        self.wait_visible(MainPageLocators.ACCOUNT_QUIT).click()
        self.wait_visible(MainPageLocators.BUTTON_ACCEPT).click()

    def collapse_navigator_directories(self):
        action = ActionChains(self.driver)
        navigator = self.wait_visible(MainPageLocators.NAVIGATOR)
        action.context_click(navigator)
        action.move_by_offset(5, 5)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.RETURN)
        action.perform()

    def open_daily_mode(self):
        completed_work = self.find(MainPageLocators.COMPLETED_WORK)
        ActionChains(self.driver).double_click(completed_work).perform()
        daily_mode = self.find(MainPageLocators.DAILY_MODE)
        ActionChains(self.driver).double_click(daily_mode).perform()
        # WebDriverWait(self.driver, 5).until(
        #     expected_conditions.visibility_of_all_elements_located(
        #         (By.XPATH, '//div[@class="x-grid-scroll-container "]')
        #     )
        # )
        time.sleep(10)
