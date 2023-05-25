from Resources.Page_Objects.Common_Page import CommonPage
from selenium.webdriver.common.by import By
import re


class CheckoutPage(CommonPage):

    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH_BUTTON = (By.ID, "finish")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    ERROR_MESSAGE_CONTAINER = CommonPage.ERROR_MESSAGE_CONTAINER
    ORDER_COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    FIRST_NAME_ERROR_MESSAGE = "Error: First Name is required"
    LAST_NAME_ERROR_MESSAGE = "Error: Last Name is required"
    POSTAL_CODE_ERROR_MESSAGE = "Error: Postal Code is required"
    ORDER_COMPLETE_MESSAGE = "Thank you for your order!"

    ITEM_TOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def click_on_continue_button(self):
        self.click_on(locator=self.CONTINUE_BUTTON)

    def click_on_cancel_button(self):
        self.click_on(locator=self.CANCEL_BUTTON)

    def click_on_finish_button(self):
        self.click_on(locator=self.FINISH_BUTTON)

    def click_on_back_home_button(self):
        self.click_on(locator=self.BACK_HOME_BUTTON)

    def input_first_name(self, name: str):
        self.input_text(locator=self.FIRST_NAME_FIELD, text=name)

    def input_last_name(self, name: str):
        self.input_text(locator=self.LAST_NAME_FIELD, text=name)

    def input_postal_code(self, code: str or int):
        self.input_text(locator=self.POSTAL_CODE_FIELD, text=str(code))

    def verify_first_name_error_message_is_visible(self, timeout: int):
        return self.verify_error_message_is_visible(locator=self.ERROR_MESSAGE_CONTAINER,
                                                    expected_error_message=self.FIRST_NAME_ERROR_MESSAGE,
                                                    timeout=timeout)

    def verify_last_name_error_message_is_visible(self, timeout: int):
        return self.verify_error_message_is_visible(locator=self.ERROR_MESSAGE_CONTAINER,
                                                    expected_error_message=self.LAST_NAME_ERROR_MESSAGE,
                                                    timeout=timeout)

    def verify_postal_code_error_message_is_visible(self, timeout: int):
        return self.verify_error_message_is_visible(locator=self.ERROR_MESSAGE_CONTAINER,
                                                    expected_error_message=self.POSTAL_CODE_ERROR_MESSAGE,
                                                    timeout=timeout)

    def verify_order_complete_message_is_visible(self, timeout: int):
        return self.verify_error_message_is_visible(locator=self.ORDER_COMPLETE_HEADER,
                                                    expected_error_message=self.ORDER_COMPLETE_MESSAGE,
                                                    timeout=timeout)

    def verify_item_total(self, expected_price: float, timeout: int):
        item_total_label = self.wait_until_element_visible(locator=self.ITEM_TOTAL_LABEL, timeout=timeout)
        if bool(item_total_label):
            numbers = re.search(r"\d+\.\d+$", item_total_label.text)
            if numbers:
                return float(numbers.group()) == expected_price
            else:
                raise Exception(f"Error: Item total label doesn't contain the price")
        else:
            raise Exception(f"Error: Element {self.ITEM_TOTAL_LABEL} is not visible after {timeout} sec(s)")

    def verify_tax(self, expected_tax: float, timeout: int):
        tax_label = self.wait_until_element_visible(locator=self.TAX_LABEL, timeout=timeout)
        if bool(tax_label):
            numbers = re.search(r"\d+\.\d+$", tax_label.text)
            if numbers:
                return float(numbers.group()) == expected_tax
            else:
                raise Exception(f"Error: Item total label doesn't contain the price")
        else:
            raise Exception(f"Error: Element {self.TAX_LABEL} is not visible after {timeout} sec(s)")

    def verify_total(self, expected_total: float, timeout: int):
        total_label = self.wait_until_element_visible(locator=self.TOTAL_LABEL, timeout=timeout)
        if bool(total_label):
            numbers = re.search(r"\d+\.\d+$", total_label.text)
            if numbers:
                return float(numbers.group()) == expected_total
            else:
                raise Exception(f"Error: Item total label doesn't contain the price")
        else:
            raise Exception(f"Error: Element {self.TOTAL_LABEL} is not visible after {timeout} sec(s)")

    @staticmethod
    def calculate_tax(price: float, percentage=8):
        return float("%.2f" % (price * percentage / 100))
