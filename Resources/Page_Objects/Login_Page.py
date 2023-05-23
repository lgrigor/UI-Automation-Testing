from Resources.Page_Objects.Common_Page import CommonPage
from selenium.webdriver.common.by import By


class LoginPage(CommonPage):

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    INVENTORY_PAGE = (By.ID, "inventory_container")

    ERROR_MESSAGE_CLOSE_BUTTON = CommonPage.ERROR_MESSAGE_CLOSE_BUTTON
    ERROR_MESSAGE_CONTAINER = CommonPage.ERROR_MESSAGE_CONTAINER

    BLOCKED_USER_ERROR_MESSAGE = "Epic sadface: Sorry, this user has been locked out."
    MISSING_USERNAME_ERROR_MESSAGE = "Epic sadface: Username is required"
    MISSING_PASSWORD_ERROR_MESSAGE = "Epic sadface: Password is required"
    WRONG_USER_OR_PASS_ERROR_MESSAGE = "Epic sadface: Username and password do not match any user in this service"

    def navigate_to_home_page(self):
        self.navigate_to(url=self.BASE_URL)

    def input_username(self, username):
        self.input_text(locator=self.USERNAME_FIELD, text=username)

    def input_password(self, password):
        self.input_text(locator=self.PASSWORD_FIELD, text=password)

    def click_on_login_button(self):
        self.click_on(locator=self.LOGIN_BUTTON)

    def verify_inventory_page_is_visible(self, timeout):
        return bool(self.wait_until_element_visible(locator=self.INVENTORY_PAGE, timeout=timeout))

    def verify_blocked_user_error_message_is_visible(self, timeout):
        self.verify_error_message_is_visible(locator=self.ERROR_MESSAGE_CONTAINER,
                                             expected_error_message=self.BLOCKED_USER_ERROR_MESSAGE,
                                             timeout=timeout)

    def verify_missing_username_error_message_is_visible(self, timeout):
        self.verify_error_message_is_visible(locator=self.ERROR_MESSAGE_CONTAINER,
                                             expected_error_message=self.MISSING_USERNAME_ERROR_MESSAGE,
                                             timeout=timeout)

    def verify_missing_password_error_message_is_visible(self, timeout):
        self.verify_error_message_is_visible(locator=self.ERROR_MESSAGE_CONTAINER,
                                             expected_error_message=self.MISSING_PASSWORD_ERROR_MESSAGE,
                                             timeout=timeout)

    def verify_wrong_username_or_password_error_message_is_visible(self, timeout):
        self.verify_error_message_is_visible(locator=self.ERROR_MESSAGE_CONTAINER,
                                             expected_error_message=self.WRONG_USER_OR_PASS_ERROR_MESSAGE,
                                             timeout=timeout)

    def verify_error_close_button_is_visible(self, timeout):
        return bool(self.wait_until_element_visible(locator=self.ERROR_MESSAGE_CLOSE_BUTTON, timeout=timeout))
