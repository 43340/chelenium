from chelenium.chelenium import *



class AuthPage(PageElement):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'page_label': (By.XPATH, "//h1[@class='page-heading']"),
        'reg_form': (By.XPATH, "//form[@id='create-account_form']"),
        'login_form': (By.XPATH, "//form[@id='login_form']"),
        'reg_email_input': (By.XPATH, "//input[@id='email_create']"),
        'reg_button': (By.XPATH, '//*[@id="SubmitCreate"]'),
        'login_email_input': (By.XPATH, "//input[@id='email']"),
        'login_password_input': (By.XPATH, "//input[@id='passwd']"),
        'login_button': (By.XPATH, '//*[@id="SubmitLogin"]'),
        'error_alert': (By.CSS_SELECTOR, "#center_column > div.alert.alert-danger")
    }

    @property
    def is_page_loaded(self):
        return True if (self.page_label.text == "AUTHENTICATION" and
                        self.reg_form.is_displayed() and
                        self.login_form.is_displayed()) else False

    @property
    def is_error_alert_displayed(self):
        return True if self.error_alert.is_displayed() else False

    @property
    def error_message(self):
        if self.is_error_alert_displayed:
            return self.error_alert.text

    def register(self, data):
        actions.send_text(self.reg_email_input, (data.get('email')))
        actions.click(self.reg_button)

    def login(self, data):
        actions.send_text(self.login_email_input, (data.get('email')))
        actions.send_text(self.login_password_input, (data.get('password')))
        actions.click(self.login_button)