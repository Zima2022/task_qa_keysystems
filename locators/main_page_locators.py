from selenium.webdriver.common.by import By


class MainPageLocators:
    # Панель навигатора
    NAVIGATOR = (By.CSS_SELECTOR, '#navigatorTree-body')
    BUTTON_OK = (By.XPATH, '//div[@role="dialog"]//a')
    # Аккаунт, под которы пользователь авторизован в приложении
    ACCOUNT = (By.CSS_SELECTOR, '#ks-core-dashboard-header-useraccountbtn-1114-btnInnerEl')
    # Меню "Выйти" из аккаунта
    ACCOUNT_QUIT = (By.XPATH, '//span[text()="Выйти"]')
    # Кнопка ОК диалогового окна для подтверждения выхода из аккаунта
    BUTTON_ACCEPT = (By.XPATH, '//div[@role="dialog"]//a[1]')
    # Элементы на панели навигатора
    NAVIGATOR_ELEMENTS = (By.CSS_SELECTOR, '.x-tree-node-text span')
    # Каталог "УЧЕТ ВЫПОЛНЕННЫХ РАБОТ" в навигаторе
    COMPLETED_WORK = (By.XPATH, '//tr[@data-qtip="УЧЕТ ВЫПОЛНЕННЫХ РАБОТ"]')
    # Режим "Ежедневный" на панели навигатора
    DAILY_MODE = (By.XPATH, '//tr[@data-qtip="Ежедневный"]')
    # Открытая вкладка "Ежедневный" на рабочем столе
    TAB_DAILY_MODE = (By.XPATH, '//a[@role="tab"]//span[text()="Ежедневный"]')


