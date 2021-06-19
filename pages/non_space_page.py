from selenium.webdriver.common.by import By
from base_page import BasePage

BUTTON = (By.XPATH, "//button[text()='My Button']")


class NonSpacePage(BasePage):

    def should_be_button(self):
        try:
            self.find_element(BUTTON)
            return True
        except:
            return False