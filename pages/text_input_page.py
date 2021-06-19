from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



INPUT_FIELD = (By.XPATH, "//input[@class='form-control']")
NEW_NAME = "hello world button"
BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")


class TextInputPage(BasePage):

    def send_keys_in_a_diff_way(self):
        field = self.find_element(INPUT_FIELD)
        ActionChains(self.driver).move_to_element(field).click().send_keys_to_element(field, NEW_NAME).perform()

    def submit_new_button_name(self):
        self.press_button_with_action_chains(BUTTON)

    def should_be_new_button_name(self):
        text = self.find_element(BUTTON).text
        return text == NEW_NAME
