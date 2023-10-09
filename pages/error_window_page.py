from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ErrorWindowPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._button = (By.CSS_SELECTOR, '#button-1059-btnInnerEl')
        self._error_window_locator = (By.CSS_SELECTOR, '#ks-clienterror-window-1050')

    def close(self):
        try:
            self.wait_visible(self._error_window_locator)
            self.find(self._button).click()
        except TimeoutException:
            pass
