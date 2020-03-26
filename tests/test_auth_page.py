import time
import pytest
from pages.home_page import HomePage
from pages.auth_page import AuthPage
from pages.profile_page import ProfilePage
from chelenium.asserts import *
from chelenium import page_actions as actions
from utilities import data_provider as dp


class TestAuthPage:

    def test_login_correct_credentials(self, driver):
        data = dp.test_data_provider("login", "login_correct_credentials")
        page = HomePage(driver)
        assert_true(page.is_page_loaded)
        actions.click(page.sign_in_button)

        page = AuthPage(driver)
        assert_true(page.is_page_loaded)
        page.login(data)
        page = ProfilePage(driver)
        assert_true(page.is_page_loaded)

    def test_login_wrong_credentials(self, driver):
        data = dp.test_data_provider("login", "login_wrong_credentials")
        page = HomePage(driver)
        assert_true(page.is_page_loaded)
        actions.click(page.sign_in_button)

        page = AuthPage(driver)
        assert_true(page.is_page_loaded)
        page.login(data)
        assert_true(page.is_error_alert_displayed)
        assert_equal(page.error_message, "There is 1 error\nAuthentication failed.")

    def test_login_missing_email(self, driver):
        data = dp.test_data_provider("login", "login_no_email")
        page = HomePage(driver)
        assert_true(page.is_page_loaded)
        actions.click(page.sign_in_button)

        page = AuthPage(driver)
        assert_true(page.is_page_loaded)
        page.login(data)
        assert_true(page.is_error_alert_displayed)
        assert_equal(page.error_message, "There is 1 error\nAn email address required.")

    def test_login_missing_password(self, driver):
        data = dp.test_data_provider("login", "login_no_password")
        page = HomePage(driver)
        assert_true(page.is_page_loaded)
        actions.click(page.sign_in_button)

        page = AuthPage(driver)
        assert_true(page.is_page_loaded)
        page.login(data)
        assert_true(page.is_error_alert_displayed)
        assert_equal(page.error_message, "There is 1 error\nPassword is required.")

    def test_login_missing_email_and_password(self, driver):
        data = dp.test_data_provider("login", "login_no_email_and_password")
        page = HomePage(driver)
        assert_true(page.is_page_loaded)
        actions.click(page.sign_in_button)

        page = AuthPage(driver)
        assert_true(page.is_page_loaded)
        page.login(data)
        assert_true(page.is_error_alert_displayed)
        assert_equal(page.error_message, "There is 1 error\nAn email address required.")
