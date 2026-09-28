import pytest
from pages.login_page import LoginPage
from utils.read_properties import ReadConfig
from utils.csv_reader import read_data_from_csv

@pytest.mark.usefixtures("setup")
class TestLogin:
    baseURL = ReadConfig.get_application_url()

    @pytest.mark.parametrize("username,password,expected", read_data_from_csv("logindata.csv"))
    def test_login_ddt(self, username, password, expected):
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.click_my_account()
        lp.click_login_link()
        lp.set_email(username)
        lp.set_password(password)
        lp.click_login()
        
        target_page_exists = lp.is_my_account_page_exists()
        
        if expected.lower() == 'pass':
            if target_page_exists:
                assert True
            else:
                assert False, "Login failed but expected to pass"
        elif expected.lower() == 'fail':
            if target_page_exists:
                assert False, "Login passed but expected to fail"
            else:
                warning_msg = lp.get_warning_message()
                assert "Warning: No match for E-Mail Address and/or Password." in warning_msg, f"Warning message mismatch: {warning_msg}"
                assert True
