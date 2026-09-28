from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
    def click_element(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()
        
    def enter_text(self, by_locator, text):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)
        
    def get_element_text(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_element_visible(self, by_locator):
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False
