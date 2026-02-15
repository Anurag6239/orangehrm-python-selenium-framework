import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config.config import BASE_URL, IMPLICIT_WAIT

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.get(BASE_URL)
    yield driver
    driver.quit()