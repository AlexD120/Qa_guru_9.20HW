import pytest
from selene import browser
from selenium import webdriver

BASE_URL = "https://demowebshop.tricentis.com/"


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    driver_options = webdriver.ChromeOptions()
    browser.config.driver_options = driver_options
    browser.config.window_width = 1440
    browser.config.window_height = 900
    browser.open(BASE_URL)

    yield browser

    browser.quit()
