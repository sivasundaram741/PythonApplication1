from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def fill_checkout_details(self, first_name, last_name, postal_code):
        self.wait_for_element(By.ID, 'first-name').send_keys(first_name)
        self.wait_for_element(By.ID, 'last-name').send_keys(last_name)
        self.wait_for_element(By.ID, 'postal-code').send_keys(postal_code)

    def click_continue_button(self):
        self.wait_for_element(By.ID, 'continue').click()

    def verify_checkout_overview(self):
        return self.wait_for_element(By.CLASS_NAME, 'summary_info_label').is_displayed()

    def finish_checkout(self):
        self.wait_for_element(By.ID, 'finish').click()

