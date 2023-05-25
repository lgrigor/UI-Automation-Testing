from Resources.Page_Objects.Login_Page import LoginPage
import allure
import pytest


@pytest.mark.ui
@pytest.mark.login
class TestLogin(LoginPage):

    @allure.title("Test Login With Standard User")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_standard_user_0101(self, request):
        self.open_browser(request)
        self.navigate_to_home_page()
        self.input_username(username=self.STANDARD_USERNAME)
        self.input_password(password=self.PASSWORD)
        self.click_on_login_button()
        assert self.verify_inventory_page_is_visible(timeout=5)

    @allure.title("Test Login With Blocked User")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_blocked_user_0102(self, request):
        self.open_browser(request)
        self.navigate_to_home_page()
        self.input_username(username=self.BLOCKED_USERNAME)
        self.input_password(password=self.PASSWORD)
        self.click_on_login_button()
        assert self.verify_blocked_user_error_message_is_visible(timeout=5)
        assert self.verify_error_close_button_is_visible(timeout=5)

    @allure.title("Test Loging Without Username")
    @allure.severity(allure.severity_level.MINOR)
    def test_login_without_username_0103(self, request):
        self.open_browser(request)
        self.navigate_to_home_page()
        self.input_password(password=self.PASSWORD)
        self.click_on_login_button()
        assert self.verify_missing_username_error_message_is_visible(timeout=5)
        assert self.verify_error_close_button_is_visible(timeout=5)

    @allure.title("Test Loging Without Password")
    @allure.severity(allure.severity_level.MINOR)
    def test_login_without_password_0104(self, request):
        self.open_browser(request)
        self.navigate_to_home_page()
        self.input_username(username=self.STANDARD_USERNAME)
        self.click_on_login_button()
        assert self.verify_missing_password_error_message_is_visible(timeout=5)
        assert self.verify_error_close_button_is_visible(timeout=5)

    @allure.title("Test Loging Wrong Username or Password")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize("username, password", [
        (LoginPage.STANDARD_USERNAME, "fake_password"),
        ("fake_username", LoginPage.PASSWORD),
        ("fake_username", "fake_password"),
    ])
    def test_login_bruteforce_0105(self, username, password, request):
        self.open_browser(request)
        self.navigate_to_home_page()
        self.input_username(username=username)
        self.input_password(password=password)
        self.click_on_login_button()
        assert self.verify_wrong_username_or_password_error_message_is_visible(timeout=5)
        assert self.verify_error_close_button_is_visible(timeout=5)
