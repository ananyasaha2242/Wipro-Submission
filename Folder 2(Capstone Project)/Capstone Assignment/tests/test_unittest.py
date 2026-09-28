import unittest
from selenium import webdriver

from pages.login_page import LoginPage
from utils.read_properties import ReadConfig


class TestLoginUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Open Chrome browser
        cls.driver = webdriver.Chrome()

        # Maximize browser
        cls.driver.maximize_window()

        # Read application URL from config.ini
        cls.baseURL = ReadConfig.get_application_url()

    def test_login_page(self):
        # Open the application
        self.driver.get(self.baseURL)

        # Create Login Page object
        lp = LoginPage(self.driver)

        # Open My Account -> Login
        lp.click_my_account()
        lp.click_login_link()

        # Check that Login page is opened
        self.assertIn("Login", self.driver.title)

    @classmethod
    def tearDownClass(cls):
        # Close browser
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()