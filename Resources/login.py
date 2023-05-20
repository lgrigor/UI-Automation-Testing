from Resources.common import Common
from selenium.webdriver.common.by import By


class Login(Common):

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    INVENTORY_PAGE = (By.ID, "inventory_container")

    def navigate_to_home_page(self):
        self.navigate_to(url=self.BASE_URL)

    def input_username(self, username):
        self.input_text(locator=self.USERNAME_FIELD, text=username)

    def input_password(self, password):
        self.input_text(locator=self.PASSWORD_FIELD, text=password)

    def click_on_login_button(self):
        self.click_on(locator=self.LOGIN_BUTTON)

    def verify_inventory_page_is_visible(self, timeout):
        return self.wait_until_element_visible(locator=self.INVENTORY_PAGE, timeout=timeout)
