import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_sessionstart(session):
    load_dotenv()


@pytest.fixture(scope="function")
def driver():
    # options_chrome = webdriver.ChromeOptions()
    # options_chrome.add_argument('--headless')
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    yield driver
    driver.quit()
