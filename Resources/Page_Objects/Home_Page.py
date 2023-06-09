from Resources.Page_Objects.Common_Page import CommonPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class HomePage(CommonPage):

    ADD_TO_CART_BUTTON = (By.XPATH, "//div[text()='{}']/following::button[contains(@id, 'add-to-cart')][1]")
    REMOVE_BUTTON = (By.XPATH, "//div[text()='{}']/following::button[contains(@id, 'remove')][1]")
    PRICE_LABEL = (By.XPATH, "//div[text()='{}']/following::div[contains(@class, 'inventory_item_price')][1]")

    SHOPPING_BASKET = (By.ID, "shopping_cart_container")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_on_add_to_cart_button(self, product: str, timeout=5):
        method, locator = self.ADD_TO_CART_BUTTON
        product_add_to_cart_locator = (method, locator.format(product))
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(product_add_to_cart_locator)).click()
        except TimeoutException:
            raise Exception(f"Error: Element {product_add_to_cart_locator} is not visible after {timeout} sec(s)")

    def click_on_remove_button(self, product: str, timeout=5):
        method, locator = self.REMOVE_BUTTON
        product_add_to_cart_locator = (method, locator.format(product))
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(product_add_to_cart_locator)).click()
        except TimeoutException:
            raise Exception(f"Error: Element {product_add_to_cart_locator} is not visible after {timeout} sec(s)")

    def click_on_basket(self):
        self.click_on(locator=self.SHOPPING_BASKET)

    def click_on_checkout_button(self):
        self.click_on(locator=self.CHECKOUT_BUTTON)

    def get_product_price(self, product: str, timeout=5):
        method, locator = self.PRICE_LABEL
        product_price_locator = (method, locator.format(product))
        price = self.wait_until_element_visible(locator=product_price_locator, timeout=timeout)
        if bool(price):
            return float(price.text[1:])  # Remove dollar sign at the beginning
        else:
            raise Exception(f"Error: Element {product_price_locator} is not visible after {timeout} sec(s)")

    def verify_remove_button_is_visible(self, product: str, timeout=5):
        method, locator = self.REMOVE_BUTTON
        product_remove_locator = (method, locator.format(product))
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(product_remove_locator))
            return True
        except TimeoutException:
            return False

    def verify_add_to_cart_button_is_visible(self, product: str, timeout=5):
        method, locator = self.ADD_TO_CART_BUTTON
        product_remove_locator = (method, locator.format(product))
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(product_remove_locator))
            return True
        except TimeoutException:
            return False

    def verify_shopping_basket_count(self, expected_count: int, timeout=5):
        try:
            basket = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.SHOPPING_BASKET))
            if not expected_count:
                return basket.text == ""
            else:
                return int(basket.text) == expected_count
        except TimeoutException:
            raise Exception(f"Error: Element {self.SHOPPING_BASKET} is not visible after {timeout} sec(s)")
