import pytest
from utils.webdriver_setup import WebDriverSetup
from pages.cart_page import CartPage
from pages.login_page import LoginPage

@pytest.fixture(scope="class")
def test_setup(request):
    setup = WebDriverSetup()
    request.cls.driver = setup.get_driver()
    login_page = LoginPage(request.cls.driver)
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")
    yield
    setup.quit_driver()

@pytest.mark.usefixtures("test_setup")
class TestCart:
    def test_cart_verification(self):
        cart_page = CartPage(self.driver)
        cart_page.click_cart_button()
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) == 4, "Cart should contain 4 items"

