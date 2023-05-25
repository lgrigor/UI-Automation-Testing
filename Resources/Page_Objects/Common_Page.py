from Resources.Data.Data import Data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CommonPage(Data):
    ERROR_MESSAGE_CONTAINER = (By.XPATH, "//h3[@data-test='error']")
    ERROR_MESSAGE_CLOSE_BUTTON = (By.CLASS_NAME, "error-button")

    def open_browser(self, request):
        self.driver = request.getfixturevalue("test_setup_teardown")

    def navigate_to(self, url):
        self.driver.get(url)

    def input_text(self, locator: tuple, text: str, timeout=5, clear=True):
        input_field = self.wait_until_element_visible(locator=locator, timeout=timeout)
        if bool(input_field):
            if clear:
                input_field.clear()
            input_field.send_keys(text)
        else:
            raise Exception(f"Error: Input field {locator} is not visible after {timeout} sec(s)")

    def click_on(self, locator: tuple, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)).click()
        except TimeoutException:
            raise Exception(f"Error: Input field {locator} is not visible after {timeout} sec(s)")

    def wait_until_element_visible(self, locator: tuple, timeout: int):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            print(f"Warning: Element {locator} is not visible after {timeout} sec(s)")
            return False

    def verify_error_message_is_visible(self, locator: tuple, expected_error_message: str, timeout: int):
        error_message = self.wait_until_element_visible(locator=locator, timeout=timeout)
        if bool(error_message):
            return error_message.text == expected_error_message
        else:
            return False
