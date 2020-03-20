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
        self.first_name_01.send_keys(data.get("first_name"))
        self.last_name_01.send_keys(data.get("last_name"))
     #  self.email.send_keys(data.get("email"))
        self.password.send_keys(data.get("password"))
        self.dob_day.send_keys(data.get("dob_day"))
        self.dob_month.send_keys(data.get("dob_month"))
        self.dob_year.send_keys(data.get("dob_year"))
     #   self.first_name_02.send_keys(data.get("first_name_02"))
     #   self.last_name_02.send_keys(data.get("last_name_02"))
        self.company.send_keys(data.get("company"))
        self.address_01.send_keys(data.get("address1"))
        self.address_02.send_keys(data.get("address2"))
        self.city.send_keys(data.get("city"))
        self.state.send_keys(data.get("state"))
        self.postcode.send_keys(data.get("postcode"))
        self.country.send_keys(data.get("country"))
        self.phone.send_keys(data.get("phone"))
        self.alias.send_keys(data.get("alias"))
        self.btn_register.click()
