from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """Открывает страницу, хранящуюся в self.url."""
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """Возвращает элемент html-страницы по локатору.

        :param locator: локатор
        :param timeout: время ожидания (в секундах) появления элемента в DOM
         """
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
