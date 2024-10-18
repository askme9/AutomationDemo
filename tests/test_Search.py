from tests.BaseTest import BaseTest
from pages.HomePage import *
from pages.BasePage import *
from pages.SearchPage import *
import pytest

@pytest.mark.usefixtures('setup_and_teardown')
class TestSearch(BaseTest):

    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field('hp')
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        product_status = search_page.display_status_of_valid_product()
        assert product_status,True


    def test_search_for_a_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field('mobile')
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        no_product_message = search_page.retrieve_no_product_message()
        assert no_product_message,"There is no product that matches the search criteria."

    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field('')
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        no_product_message = search_page.retrieve_no_product_message()
        assert no_product_message,"There is no product that matches the search criteria."

