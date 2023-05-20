from Resources.login import Login
import allure
import pytest


class TestLogin(Login):

    @allure.title("Test Login With Standard User")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_user_successful(self, request):
        self.open_browser(request)
        self.navigate_to_home_page()
        self.input_username(self.STANDARD_USERNAME)
        self.input_password(self.PASSWORD)
        self.click_on_login_button()
        assert self.verify_inventory_page_is_visible(5)


