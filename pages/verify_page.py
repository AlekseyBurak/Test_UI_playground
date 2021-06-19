from selenium.common.exceptions import NoSuchElementException

from base_page import BasePage
from selenium.webdriver.common.by import By

WELCOME_TEXT = (By.XPATH, "//span[normalize-space(.)='Welcome UserName!']")


class VerifyPage(BasePage):

    def should_be_welcome_text(self):
        try:
            self.find_element(WELCOME_TEXT)
            return True
        except NoSuchElementException:
            return False
