import pytest
from utils.webdriver_setup import WebDriverSetup
from pages.login_page import LoginPage

@pytest.fixture(scope="class")
def test_setup(request):
    setup = WebDriverSetup()
    request.cls.driver = setup.get_driver()
    yield
    setup.quit_driver()

@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        login_page.login("standard_user", "secret_sauce")
        assert login_page.verify_login_success(), "Login Failed!"

