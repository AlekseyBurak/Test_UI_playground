from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException

BUTTON = (By.XPATH, "//button[@class='btn btn-success']")


class HiddenLayersPage(BasePage):

    def press_green_button(self):
        self.press_button_with_execute_script(BUTTON)

    def should_be_untouchable(self):
        try:
            self.find_element(BUTTON).click()
            return False
        except ElementClickInterceptedException:
            return True
