import pytest
from selenium import webdriver

DRIVER_PATH = "/Selenium_Lesson_16/drivers/chromedriver.exe"
SITE_PATH = "https://rioran.github.io/ru_vowels_filter/main.html"


@pytest.fixture()
def chrome_driver():
    """Start the chrome driver"""
    chrome_driver = webdriver.Chrome(DRIVER_PATH)
    chrome_driver.get(SITE_PATH)
    return chrome_driver
