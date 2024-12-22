from selenium.webdriver.common.by import By
from pages.base_page.py import basePage # type: ignore

class LoginPage(basePage):
    URL = 'https://www.saucedemo.com/'

    def open_login_page(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.wait_for_element(By.ID, 'user-name').send_keys(username)
        self.wait_for_element(By.ID, 'password').send_keys(password)
        self.wait_for_element(By.ID, 'login-button').click()

    def verify_login_success(self):
        return "inventory" in self.driver.current_url

