from selenium.webdriver import ActionChains

from base_page import BasePage
from selenium.webdriver.common.by import By

CLICK_ME_TEXT = (By.XPATH, "//a[@class='text-primary']")
CLICKABLE_TEXT = (By.XPATH, "//a[@class='text-warning']")
COUNTER = (By.XPATH, "//span[@class='badge badge-light']")
NUM = 2


class MouseOverPage(BasePage):

    def click_this_text_n_times(self):
        text_to_click = self.find_element(CLICK_ME_TEXT)
        ActionChains(self.driver).move_to_element(text_to_click).perform()
        for _ in range(NUM):
            real_place_to_click = self.find_element(CLICKABLE_TEXT)
            ActionChains(self.driver).click(real_place_to_click).perform()

    def should_be_correct_counter(self):
        counter = self.find_element(COUNTER).text
        return counter == str(NUM)