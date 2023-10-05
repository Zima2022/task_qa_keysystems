from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ErrorWindowPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._button = (By.CSS_SELECTOR, '#button-1059-btnInnerEl')

    def close(self):
        self.find(self._button).click()
