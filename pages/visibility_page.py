from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base_page import BasePage

HIDE_BUTTON = (By.XPATH, "//button[@id='hideButton']")

REMOVED_BUTTON = (By.XPATH, "//button[@id='removedButton']")
ZERO_WIDTH_BUTTON = (By.XPATH, "//button[@id='zeroWidthButton']")
OWERLAPPED_BUTTON = (By.XPATH, "//button[@id='overlappedButton']")
OPACITY_0_BUTTON = (By.XPATH, "//button[@id='transparentButton']")
INVISIBLE_BUTTON = (By.XPATH, "//button[@id='invisibleButton']")
NONE_DISPLAY_BUTTON = (By.XPATH, "//button[@id='notdisplayedButton']")
OFF_SCREEN_BUTTON = (By.XPATH, "//button[@id='offscreenButton']")


LIST_OF_BUTTONS = [
    REMOVED_BUTTON,
    ZERO_WIDTH_BUTTON,
    OWERLAPPED_BUTTON,
    OPACITY_0_BUTTON,
    INVISIBLE_BUTTON,
    NONE_DISPLAY_BUTTON,
    OFF_SCREEN_BUTTON
]


class VisibilityPage(BasePage):

    def press_hide_button(self):
        self.press_button_with_execute_script(HIDE_BUTTON)

    def should_disappear(self):
        try:
            for item in LIST_OF_BUTTONS:
                self.find_button(item, time=1)
            return False
        except TimeoutException:
            return True