from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base_page import BasePage

BUTTON = (By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")


class ClassArtPage(BasePage):

    def press_blue_button(self):
        self.press_button_with_execute_script(BUTTON)

    def should_find_button(self):
        try:
            self.find_button(BUTTON)
            return True
        except TimeoutException:
            return False
