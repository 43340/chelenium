import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(30)
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
