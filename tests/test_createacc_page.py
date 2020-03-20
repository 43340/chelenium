from utilities import data_provider as provider
from tests.test_base import BaseTest
from pages.home_page import HomePage
from pages.auth_page import AuthPage
from pages.createacc_page import CreateAccPage
from pages.profile_page import ProfilePage
import time

class CreateAccPageTest(BaseTest):

    def test_valid_acc_creation(self):
        self.data = provider.test_data_provider("register", "valid_acc_creation")
        homepage = HomePage(self.driver)
        authpage = AuthPage(self.driver)
        createaccpage = CreateAccPage(self.driver)
        profilepage = ProfilePage(self.driver)

        self.assertTrue(homepage.is_page_loaded)
        homepage.sign_in_button.click()

        self.assertTrue(authpage.is_page_loaded)
        authpage.register(self.data)

        self.assertTrue(createaccpage.is_page_loaded)
        createaccpage.fill_up_form(self.data)

        self.assertTrue(profilepage.is_page_loaded())
        time.sleep(3)
