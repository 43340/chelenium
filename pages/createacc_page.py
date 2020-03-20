from chelenium.chelenium import *

class CreateAccPage(PageElement):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'page_header': (By.XPATH, "//h1[@class='page-heading']"),
        'first_name_01': (By.XPATH, "//input[@id='customer_firstname']"),
        'last_name_01':(By.XPATH, "//input[@id='customer_lastname']"),
        'email':(By.XPATH, "//input[@id='email']"),
        'password': (By.XPATH, "//input[@id='passwd']"),
        'dob_day': (By.XPATH, "//select[@id='days']"),
        'dob_month': (By.XPATH, "//select[@id='months']"),
        'dob_year': (By.XPATH, "//select[@id='years']"),
        'first_name_02': (By.XPATH, "//input[@id='firstname']"),
        'last_name_02':(By.XPATH, "//input[@id='lastname']"),
        'company': (By.XPATH, "//input[@id='company']"),
        'address_01': (By.XPATH, "//input[@id='address1']"),
        'address_02':(By.XPATH, "//input[@id='address2']"),
        'city': (By.XPATH, "//input[@id='city']"),
        'state': (By.XPATH, "//select[@id='id_state']"),
        'postcode': (By.XPATH, "//input[@id='postcode']"),
        'country': (By.XPATH, "//select[@id='id_country']"),
        'phone': (By.XPATH, "//input[@id='phone_mobile']"),
        'alias': (By.XPATH, "//input[@id='alias']"),
        'btn_register': (By.XPATH, "//button[@id='submitAccount']")
    }

    def is_page_loaded(self):
        time.sleep(5)
        return True if (self.page_header.text == "Create an account" and
                        self.first_name_01.is_displayed and
                        self.last_name_01.is_displayed) else False

    def fill_up_form(self, data):
        actions.send_text(self.first_name_01, (data.get("first_name")))
        actions.send_text(self.last_name_01, (data.get("last_name")))
     #  actions.send_text(self.email, (data.get("email")))
        actions.send_text(self.password, (data.get("password")))
        actions.send_text(self.dob_day, (data.get("dob_day")))
        actions.send_text(self.dob_month, (data.get("dob_month")))
        actions.send_text(self.dob_year, (data.get("dob_year")))
     #   actions.send_text(self.first_name_02, (data.get("first_name_02")))
     #   actions.send_text(self.last_name_02, (data.get("last_name_02")))
        actions.send_text(self.company, (data.get("company")))
        actions.send_text(self.address_01, (data.get("address1")))
        actions.send_text(self.address_02, (data.get("address2")))
        actions.send_text(self.city, (data.get("city")))
        actions.send_text(self.state, (data.get("state")))
        actions.send_text(self.postcode, (data.get("postcode")))
        actions.send_text(self.country, (data.get("country")))
        actions.send_text(self.phone, (data.get("phone")))
        actions.send_text(self.alias, (data.get("alias")))
        actions.click(self.btn_register)
