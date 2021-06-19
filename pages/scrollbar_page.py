from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")


class ScrollBarPage(BasePage):

    def scroll_to_button(self):
        target = self.find_element(BUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.perform()

    def can_click_button(self):
        try:
            self.press_button_with_execute_script(BUTTON)
            return True
        except TimeoutException:
            return False
