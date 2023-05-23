from Resources.Page_Objects.Login_Page import LoginPage
from Resources.Page_Objects.Home_Page import HomePage
import allure
import pytest


@pytest.mark.ui
@pytest.mark.products
class TestProducts(HomePage, LoginPage):

    @allure.title("Test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_to_cart_product_0001(self, request):
        self.open_browser(request)
        self.navigate_to_home_page()
        self.input_username(username=self.STANDARD_USERNAME)
        self.input_password(password=self.PASSWORD)
        self.click_on_login_button()
        assert self.verify_shopping_basket_count(0)

        self.click_on_add_to_cart_button("Sauce Labs Backpack")
        assert self.verify_remove_button_is_visible("Sauce Labs Backpack")
        assert self.verify_shopping_basket_count(1)

        self.click_on_add_to_cart_button("Sauce Labs Bike Light")
        assert self.verify_remove_button_is_visible("Sauce Labs Bike Light")
        assert self.verify_shopping_basket_count(2)

    @allure.title("Test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_product_0002(self, request):
        self.open_browser(request)
        self.navigate_to_home_page()
        self.input_username(username=self.STANDARD_USERNAME)
        self.input_password(password=self.PASSWORD)
        self.click_on_login_button()
        self.click_on_add_to_cart_button(product="Sauce Labs Backpack")
        self.click_on_add_to_cart_button(product="Sauce Labs Bike Light")
        self.click_on_remove_button(product="Sauce Labs Backpack")
        assert self.verify_add_to_cart_button_is_visible(product="Sauce Labs Backpack")
        assert self.verify_shopping_basket_count(1)

        self.click_on_basket()
        self.click_on_remove_button(product="Sauce Labs Bike Light")
        assert self.verify_shopping_basket_count(0)
