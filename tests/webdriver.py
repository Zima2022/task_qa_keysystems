# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# class WebDriver:
#     def __init__(self):
#         self.driver = None
#
#     def setup_method(self):
#         if self.driver is None:
#             driver_service = Service(ChromeDriverManager().install())
#             self.driver = webdriver.Chrome(service=driver_service)
#
#     def teardown_method(self):
#         if self.driver:
#             self.driver.quit()
