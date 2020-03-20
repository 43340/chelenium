from chelenium.chelenium import *


class ProfilePage(PageElement):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'page_label': (By.XPATH, "//h1[@class='page-heading']"),
    }

    def is_page_loaded(self):
        return True if self.page_label.text == "MY ACCOUNT" else False