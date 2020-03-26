import time
import pytest
from tests.test_base import BaseTest
from pages.home_page import HomePage
from pages.auth_page import AuthPage
from pages.profile_page import ProfilePage
from chelenium.chelenium import *


class TestAuthPage:

    def test_login_correct_credentials(self, driver):
        data = dp.test_data_provider("login", "login_correct_credentials")
        page = HomePage(driver)
        assert page.is_page_loaded
        actions.click(page.sign_in_button)

        page = AuthPage(driver)
        assert page.is_page_loaded
        page.login(data)
        page = ProfilePage(driver)
        assert page.is_page_loaded
        time.sleep(5)

    def test_login_wrong_credentials(self, driver):
        data = dp.test_data_provider("login", "login_wrong_credentials")
        page = HomePage(driver)
        assert page.is_page_loaded
        actions.click(page.sign_in_button)

        page = AuthPage(driver)
        assert page.is_page_loaded
        page.login(data)
        assert page.is_error_alert_displayed
        assert page.error_message == "There is 1 error\nAuthentication failed."

    def test_login_missing_email(self, driver):
        data = dp.test_data_provider("login", "login_no_email")
        page = HomePage(driver)
        assert page.is_page_loaded
        actions.click(page.sign_in_button)

        page = AuthPage(driver)
        assert page.is_page_loaded
        page.login(data)
        assert page.is_error_alert_displayed
        assert page.error_message == "There is 1 error\nAn email address required."

    def test_login_missing_password(self, driver):
        data = dp.test_data_provider("login", "login_no_password")
        page = HomePage(driver)
        assert page.is_page_loaded
        actions.click(page.sign_in_button)

        page = AuthPage(driver)
        assert page.is_page_loaded
        page.login(data)
        assert page.is_error_alert_displayed
        assert page.error_message == "There is 1 error\nPassword is required."

    def test_login_missing_email_and_password(self, driver):
        data = dp.test_data_provider("login", "login_no_email_and_password")
        page = HomePage(driver)
        assert page.is_page_loaded
        actions.click(page.sign_in_button)

        page = AuthPage(driver)
        assert page.is_page_loaded
        page.login(data)
        assert page.is_error_alert_displayed
        assert page.error_message, "There is 1 error\nAn email address required."
