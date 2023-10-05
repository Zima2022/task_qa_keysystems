from selenium.webdriver.common.by import By


class MainPageLocators:
    NAVIGATOR = (By.CSS_SELECTOR, '#ks-core-dashboard-navigationpanel-1074_header-title-textEl')
    BUTTON_OK = (By.XPATH, '//div[@role="dialog"]//a')
