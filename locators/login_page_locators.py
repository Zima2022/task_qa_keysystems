from selenium.webdriver.common.by import By


class LoginPageLocators:
    CLIENT_ERROR_WINDOW = (By.CSS_SELECTOR, '#ks-clienterror-window-1050')
    BUTTON_CLOSE = (By.CSS_SELECTOR, '#button-1059-btnInnerEl')
    LOGIN = (By.CSS_SELECTOR, '#textfield-1018-inputEl')
    PASSWORD = (By.CSS_SELECTOR, '#textfield-1019-inputEl')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#button-1022-btnInnerEl')
