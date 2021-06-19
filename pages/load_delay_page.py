from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")


class LoadDelayPage(BasePage):

    def should_be_button(self):
        try:
            self.find_button(BUTTON, time=30)
            return True
        except NoSuchElementException:
            return False
