import time
import pytest
import allure
from pages.home_page import HomePage
from pages.auth_page import AuthPage
from pages.profile_page import ProfilePage
from chelenium.asserts import *
from chelenium import page_actions as actions
from utilities import data_provider as dp


class TestAuthPage:

    @allure.title("Login test using correct credentials")
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

    @allure.title("Login test with invalid credentials")
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

    @allure.title("Login test with missing email")
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

    @allure.title("Login test with missing password")
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

    @allure.title("Login test with missing email and password")
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
