from Resources.common_page import Common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Products(Common):

    ADD_TO_CART_BUTTON = (By.XPATH, "//div[text()='{}']/following::button[contains(@id, 'add-to-cart')][1]")
    REMOVE_BUTTON = (By.XPATH, "//div[text()='{}']/following::button[contains(@id, 'remove')][1]")
    SHOPPING_BASKET = (By.ID, "shopping_cart_container")

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
