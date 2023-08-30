from selenium.webdriver.chrome.service import Service
from locators import Locators
from selenium import webdriver
import pytest
from time import sleep
from config import *


@pytest.fixture()
def browser():
    service = Service(PATH_DRIVER)
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def auth(browser):
    auth = Locators(browser)
    auth.get_site()
    yield auth


@pytest.fixture()
def auth_code(browser):
    auth_code = Locators(browser)
    auth_code.get_site_auth_code()
    yield auth_code


