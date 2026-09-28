from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    # Locators
    txt_search_name = (By.NAME, "search")
    btn_search_xpath = (By.XPATH, "//div[@id='search']//button")
    msg_no_product_xpath = (By.XPATH, "//p[contains(text(),'There is no product that matches the search criter')]")
    product_link_xpath_template = "//a[normalize-space()='{}']"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_search_query(self, query):
        self.enter_text(self.txt_search_name, query)

    def click_search(self):
        self.click_element(self.btn_search_xpath)

    def is_product_displayed(self, product_name):
        locator = (By.XPATH, self.product_link_xpath_template.format(product_name))
        return self.is_element_visible(locator)
        
    def get_no_product_message(self):
        return self.get_element_text(self.msg_no_product_xpath)
