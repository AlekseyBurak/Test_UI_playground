from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base_page import BasePage

BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")


class DynamicIdPage(BasePage):

    def can_click_dynamic_id_button(self):
        try:
            self.press_button_with_execute_script(BUTTON)
            return True
        except NoSuchElementException:
            return False
