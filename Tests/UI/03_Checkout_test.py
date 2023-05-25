from Resources.Page_Objects.Checkout_Page import CheckoutPage
from Resources.Page_Objects.Login_Page import LoginPage
from Resources.Page_Objects.Home_Page import HomePage
import allure
import pytest


@pytest.mark.ui
@pytest.mark.products
class TestProducts(HomePage, LoginPage, CheckoutPage):

    @allure.title("Test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_one_product_tax_calculation_0301(self, request):
        self.open_browser(request)
        self.navigate_to_home_page()
        self.input_username(username=self.STANDARD_USERNAME)
        self.input_password(password=self.PASSWORD)
        self.click_on_login_button()
        self.click_on_add_to_cart_button(product="Sauce Labs Backpack")
        price = self.get_product_price(product="Sauce Labs Backpack")
        tax = self.calculate_tax(price=price)
        total = price + tax
        self.click_on_basket()
        self.click_on_checkout_button()
        self.input_first_name(name="John")
        self.input_last_name(name="Doe")
        self.input_postal_code(code="00243")
        self.click_on_continue_button()
        assert self.verify_item_total(expected_price=price, timeout=5)
        assert self.verify_tax(expected_tax=tax, timeout=5)
        assert self.verify_total(expected_total=total, timeout=5)

    @allure.title("Test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_multiple_products_tax_calculation_0302(self, request):
        self.open_browser(request)
        self.navigate_to_home_page()
        self.input_username(username=self.STANDARD_USERNAME)
        self.input_password(password=self.PASSWORD)
        self.click_on_login_button()
        self.click_on_add_to_cart_button(product="Sauce Labs Backpack")
        self.click_on_add_to_cart_button(product="Sauce Labs Bike Light")
        price = self.get_product_price(product="Sauce Labs Backpack")
        price += self.get_product_price(product="Sauce Labs Bike Light")
        tax = self.calculate_tax(price=price)
        total = price + tax
        self.click_on_basket()
        self.click_on_checkout_button()
        self.input_first_name(name="John")
        self.input_last_name(name="Doe")
        self.input_postal_code(code="00243")
        self.click_on_continue_button()
        assert self.verify_item_total(expected_price=price, timeout=5)
        assert self.verify_tax(expected_tax=tax, timeout=5)
        assert self.verify_total(expected_total=total, timeout=5)

    @allure.title("Test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_buying_one_product_0303(self, request):
        self.open_browser(request)
        self.navigate_to_home_page()
        self.input_username(username=self.STANDARD_USERNAME)
        self.input_password(password=self.PASSWORD)
        self.click_on_login_button()
        self.click_on_add_to_cart_button(product="Sauce Labs Backpack")
        self.click_on_basket()
        self.click_on_checkout_button()
        self.input_first_name(name="John")
        self.input_last_name(name="Doe")
        self.input_postal_code(code="00243")
        self.click_on_continue_button()
        self.click_on_finish_button()
        assert self.verify_order_complete_message_is_visible(timeout=5)

    @allure.title("Test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_buying_multiple_products_0304(self, request):
        self.open_browser(request)
        self.navigate_to_home_page()
        self.input_username(username=self.STANDARD_USERNAME)
        self.input_password(password=self.PASSWORD)
        self.click_on_login_button()
        self.click_on_add_to_cart_button(product="Sauce Labs Backpack")
        self.click_on_add_to_cart_button(product="Sauce Labs Bike Light")
        self.click_on_basket()
        self.click_on_checkout_button()
        self.input_first_name(name="John")
        self.input_last_name(name="Doe")
        self.input_postal_code(code="00243")
        self.click_on_continue_button()
        self.click_on_finish_button()
        assert self.verify_order_complete_message_is_visible(timeout=5)
