from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    # Locators in Home Page
    search_box_field_name = "search"
    search_button_xpath = "//button[contains(@class,'btn-default')]"
    myaccount_drop_menu_xpath = "//span[text()='My Account']"
    register_option_link_text = "Register"
    login_option_link_text = "Login"


    def enter_product_into_search_box_field(self,product_name):
        self.type_into_element(product_name,'search_box_field_name',self.search_box_field_name)

    def click_on_search_button(self):
        self.element_click("search_button_xpath",self.search_button_xpath)

    def click_on_myaccount_dropdown(self):
        self.element_click('myaccount_drop_menu_xpath',self.myaccount_drop_menu_xpath)

    def select_login_option(self):
        self.element_click('login_option_link_text',self.login_option_link_text)

    def select_register_option(self):
        self.element_click('register_option_link_text',self.register_option_link_text)
        

