import pytest
from pages.search_page import SearchPage
from utils.read_properties import ReadConfig
from utils.csv_reader import read_data_from_csv

@pytest.mark.usefixtures("setup")
class TestSearch:
    baseURL = ReadConfig.get_application_url()

    @pytest.mark.parametrize("search_query,expected_result", read_data_from_csv("searchdata.csv"))
    def test_search_ddt(self, search_query, expected_result):
        self.driver.get(self.baseURL)
        sp = SearchPage(self.driver)
        sp.enter_search_query(search_query)
        sp.click_search()
        
        if expected_result == "There is no product that matches the search criteria.":
            msg = sp.get_no_product_message()
            assert expected_result in msg, f"Expected '{expected_result}' but got '{msg}'"
        else:
            is_displayed = sp.is_product_displayed(expected_result)
            assert is_displayed, f"Product '{expected_result}' was not displayed"
