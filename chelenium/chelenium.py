import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from chelenium import page_actions as actions
from utilities import data_provider as dp


class PageElement(object):

    timeout = 10
    name = ""

    def __getattr__(self, item):
        """
            Catch AttributeError and return a WebElement based on the missing attribute
            1. Matches the item to the keys in the locator: dict
            2. Try to find if element is present in the DOM
                A. If element is found:
                    a. Save the locator strategy for the element in element._locator
                    b. return element
                B. Element not found:
                    a. raise an Exception

        """
        if item in self.locators.keys():

            try:
                element = self.get_element(*self.locators[item])
                element._locator = self.locators[item]
                element._name = str(item)
                return element
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
                raise e

    def get_element(self, *locator):
        element = self.find_element(*locator)
        self.highlight_element(element)
        return element

    def highlight_element(self, element):
        if self.highlight:
            self._highlight_element(element)

    def select_element_by_text(self, text):
        select = Select(self)
        select.select_by_visible_text(text)

    def select_element_by_index(self, index):
        select = Select(self)
        select.select_by_visible_text(index)

    def select_element_by_value(self, value):
        select = Select(self)
        select.select_by_visible_text(value)

    def click(self):
        self.find_clickable_element()
        self.click()
        return self

    def send_keys(self, text):
        self.find_clickable_element()
        self.send_keys(text)
        return self

    def _highlight_element(self, element):
        self.driver.execute_script("arguments[0].style.border='2px ridge #ff0000'", element)

    def find_element(self, *locator):
        return self._find_element(*locator)

    def find_visible_element(self, *locator):
        element = self._find_element(*locator)
        return element if element.is_displayed() else None

    def find_clickable_element(self, *locator):
        element = self._find_element(*locator)
        return element if element.is_enabled() else None

    @property
    def page_title(self):
        return self.driver.title

    def _find_element(self, *locator):

        eta = time.time() + self.timeout

        while True:
            try:
                return self.driver.find_element(*locator)
            except NoSuchElementException as e:
                pass

            if time.time() >= eta:
                break
        raise TimeoutException(f"Element {locator} was not present after after {self.timeout} seconds")
