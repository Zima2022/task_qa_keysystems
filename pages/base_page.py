import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = os.getenv('URL')

    def open(self):
        """Открывает страницу, адрес которой в self.url."""
        self.driver.get(self.url)

    def find(self, locator):
        """
        Возвращает web-элемент по локатору.

        :param locator: локатор
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def is_element_visible(self, locator):
        return self.find(locator).is_displayed()

    def wait_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
