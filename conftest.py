import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data import TestData


@pytest.fixture(scope="function")
def driver():
    firefox_options = Options()
    firefox_options.set_preference("browser.privatebrowsing.autostart", True)
    driver = webdriver.Firefox(options=firefox_options)
    driver.fullscreen_window()
    driver.get(TestData.URL)
    yield driver
    driver.quit()
