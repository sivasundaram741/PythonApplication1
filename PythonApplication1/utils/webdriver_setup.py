
from selenium import webdriver
import pytest_html

class WebDriverSetup:
    def __init__(self, browser='chrome'):
        self.driver = None
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        # Add other browsers if needed

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
