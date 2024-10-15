import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()  # Инициализация Firefox
    driver.maximize_window()
    yield driver
    driver.quit()