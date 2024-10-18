from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountSuccessPage(BasePage):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    # locators
    account_creation_message_xpath = "//div[@id='content']/h1"

    def retrieve_account_creation_message(self):
        return self.retrieve_element_text('account_creation_message_xpath',self.account_creation_message_xpath)