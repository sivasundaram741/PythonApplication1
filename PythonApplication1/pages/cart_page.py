from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def click_cart_button(self):
        self.wait_for_element(By.ID, 'cart_button').click()

    def get_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME, 'cart_item')

