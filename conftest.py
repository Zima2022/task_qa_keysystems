import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_sessionstart(session):
    load_dotenv()


@pytest.fixture(scope="function")
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    # driver.implicitly_wait(5)
    yield driver
    driver.quit()
