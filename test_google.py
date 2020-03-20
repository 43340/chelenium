import unittest
from selenium import webdriver
from chelenium.chelenium import *
from chelenium import page_actions as actions


class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://bing.com')
        self.driver.set_page_load_timeout(30)

    def test_bing(self):
        homepage = HomePage(self.driver)
        homepage.search('selenium')
        self.assertEqual(homepage.page_title, "SeleniumHQ Browser Automation")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class HomePage(PageElement):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'search_box': (By.NAME, 'q'),
        'search_button': (By.CSS_SELECTOR, '#sb_form > label'),
        'official_website': (By.XPATH, "//span[contains(.,'Official site')]")
    }

    def search(self, term):
        actions.send_text(self.search_box, term)
        actions.click(self.search_button)
        actions.click(self.first_result)
