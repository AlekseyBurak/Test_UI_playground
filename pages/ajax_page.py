from selenium.webdriver.common.by import By
from base_page import BasePage

BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")
TEXT_BAR = (By.XPATH, "//p[@class='bg-success']")
TEXT_IN_THR_TEXT_BAR = "Data loaded with AJAX get request."


class AjaxPage(BasePage):
    def click_button(self):
        self.press_button_with_execute_script(BUTTON)

    def should_be_text_bellow_button(self):
        text = self.find_element(TEXT_BAR, time=20).text
        return text == TEXT_IN_THR_TEXT_BAR
