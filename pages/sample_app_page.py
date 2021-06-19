from selenium.webdriver.common.by import By
from base_page import BasePage

USER_NAME_INPUT_FIELD = (By.XPATH, "//input[@name='UserName']")
PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@name='Password']")
BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")
SUCCESS_LABEL = (By.XPATH, "//label[@class='text-success']")

USER_NAME = "test_user"
PASSWORD = "pwd"


class SampleAppPage(BasePage):

    def send_user_name(self):
        self.driver.execute_script(f"document.getElementsByName('UserName')[0].value='{USER_NAME}'")

    def send_password(self):
        self.driver.execute_script(f"document.getElementsByName('Password')[0].value='{PASSWORD}'")

    def press_login_button(self):
        self.press_button_with_execute_script(BUTTON)

    def should_be_success(self):
        succ_text = self.find_element(SUCCESS_LABEL).text
        return USER_NAME in succ_text