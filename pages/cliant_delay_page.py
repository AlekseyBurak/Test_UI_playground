from selenium.webdriver.common.by import By
from base_page import BasePage

BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")
RESPONSE_FIELD = (By.XPATH, "//p[@class='bg-success']")
RESPONSE_TEXT = "Data calculated on the client side."


class ClientDelayPage(BasePage):

    def press_button(self):
        self.press_button_with_execute_script(BUTTON)

    def should_be_response_bellow(self):
        text = self.find_element(RESPONSE_FIELD, time=20).text
        return text == RESPONSE_TEXT
