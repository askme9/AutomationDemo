from pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self,driver):
        self.driver = driver
        super.__init__(driver)

    # Locators
    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    passowrd_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_field_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button_xpath = "//input[@name='newsletter' and @value=1]"
    duplicate_email_warning_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@name='firstname']/following-sibling::div"
    last_name_warning_xpath = ""
    email_warning_xpath = ""
    telephone_warning_xpath = ""
    password_warning_xpath = ""



