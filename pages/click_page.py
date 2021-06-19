from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base_page import BasePage

BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")
GREEN_BUTTON = (By.XPATH, "//button[@class='btn btn-success']")


class ClickPage(BasePage):

    def click_bad_button(self):
        self.press_button_with_action_chains(BUTTON)

    def should_be_right_colour(self):
        try:
            self.find_element(GREEN_BUTTON)
            return True
        except NoSuchElementException:
            return False
