import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    _driver = webdriver.Chrome()
    _driver.set_page_load_timeout(30)
    _driver.maximize_window()
    _driver.get('http://automationpractice.com')

    yield _driver

    _driver.close()
    _driver.quit()