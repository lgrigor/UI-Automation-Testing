from Data.data import Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Common(Data):

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
        element = self.wait_until_element_visible(locator=locator, timeout=timeout)
        if bool(element):
            element.click()
        else:
            raise Exception(f"Error: Element {locator} is not visible after {timeout} sec(s)")

    def wait_until_element_visible(self, locator: tuple, timeout: int):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            print(f"Warning: Element {locator} is not visible after {timeout} sec(s)")
            return False
