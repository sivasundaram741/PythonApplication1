import pytest
from utils.webdriver_setup import WebDriverSetup
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage

@pytest.fixture(scope="class")
def test_setup(request):
    setup = WebDriverSetup()
    request.cls.driver = setup.get_driver()
    login_page = LoginPage(request.cls.driver)
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")
    cart_page = CartPage(request.cls.driver)
    cart_page.click_cart_button()
    yield
    setup.quit_driver()

@pytest.mark.usefixtures("test_setup")
class TestCheckout:
    def test_checkout_process(self):
        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout_details("John", "Doe", "123456")
        checkout_page.click_continue_button()
        assert checkout_page.verify_checkout_overview(), "Checkout overview not displayed!"
        self.driver.save_screenshot("checkout_overview.png")
        checkout_page.finish_checkout()

