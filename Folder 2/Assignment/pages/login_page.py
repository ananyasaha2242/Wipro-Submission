from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # Locators
    lnk_myaccount_xpath = (By.XPATH, "//span[normalize-space()='My Account']")
    lnk_login_xpath = (By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']")
    txt_email_id = (By.ID, "input-email")
    txt_password_id = (By.ID, "input-password")
    btn_login_xpath = (By.XPATH, "//input[@value='Login']")
    msg_myaccount_xpath = (By.XPATH, "//h2[normalize-space()='My Account']")
    msg_warning_xpath = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_my_account(self):
        self.click_element(self.lnk_myaccount_xpath)

    def click_login_link(self):
        self.click_element(self.lnk_login_xpath)

    def set_email(self, email):
        self.enter_text(self.txt_email_id, email)

    def set_password(self, pwd):
        self.enter_text(self.txt_password_id, pwd)

    def click_login(self):
        self.click_element(self.btn_login_xpath)

    def is_my_account_page_exists(self):
        return self.is_element_visible(self.msg_myaccount_xpath)

    def get_warning_message(self):
        if self.is_element_visible(self.msg_warning_xpath):
            return self.get_element_text(self.msg_warning_xpath)
        return ""
