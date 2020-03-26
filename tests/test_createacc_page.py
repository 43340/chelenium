from utilities import data_provider as provider
from tests.test_base import BaseTest
from pages.home_page import HomePage
from pages.auth_page import AuthPage
from pages.createacc_page import CreateAccPage
from pages.profile_page import ProfilePage
import pytest
from chelenium.asserts import *
import time

class TestCreateAccPage:

    def test_valid_acc_creation(self, driver):
        data = provider.test_data_provider("register", "valid_acc_creation")
        homepage = HomePage(driver)
        authpage = AuthPage(driver)
        createaccpage = CreateAccPage(driver)
        profilepage = ProfilePage(driver)

        assert_true(homepage.is_page_loaded)
        homepage.sign_in_button.click()

        assert_true(authpage.is_page_loaded)
        authpage.register(data)

        assert_true(createaccpage.is_page_loaded)
        createaccpage.fill_up_form(data)

        assert_true(profilepage.is_page_loaded())
        time.sleep(3)
