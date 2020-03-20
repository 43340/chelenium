from chelenium.chelenium import *


class HomePage(PageElement):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'site_logo': (By.XPATH, "//img[@alt='My Store']"),
        'sign_in_button': (By.XPATH, "//a[@class='login']")
    }

    @property
    def is_page_loaded(self):
        return True if self.site_logo.is_displayed() else False
