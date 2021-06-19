from selenium.webdriver.common.by import By
from base_page import BasePage

START_BUTTON = (By.XPATH, "//button[@id='startButton']")
STOP_BUTTON = (By.XPATH, "//button[@id='stopButton']")
PROGRESS_BAR = (By.XPATH, "//div[@id='progressBar']")


class ProgressBarPage(BasePage):

    def make_75(self):
        self.press_button_with_execute_script(START_BUTTON)
        while True:
            progress = self.find_element(PROGRESS_BAR).text
            if progress == "75%":
                self.press_button_with_execute_script(STOP_BUTTON)
                break

    def should_be_progress(self):
        text = self.find_element(PROGRESS_BAR).text
        return text == "75%"
