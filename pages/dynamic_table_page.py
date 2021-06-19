from selenium.webdriver.common.by import By
from base_page import BasePage

NAME_CELL = (By.XPATH, "//div[@role='row']/span[@role='cell'][1]")
COLUMN_HEADER = (By.XPATH, "//span[@role='columnheader']")
TARGET_ROW_NAME = "Chrome"
TARGET_LINE_NAME = "CPU"
LABEL_TO_COMPARE = (By.XPATH, "//p[@class='bg-warning']")

class DynamicTablePage(BasePage):

    def get_all_names_from_table(self):
        return self.find_elements(NAME_CELL)

    def get_all_headers(self):
        return self.find_elements(COLUMN_HEADER)

    def find_target_row_name_index(self, collection):
        for item in collection:
            if item.text == TARGET_ROW_NAME:
                return collection.index(item) + 1

    def find_target_line_name_index(self, collection):
        for item in collection:
            if item.text == TARGET_LINE_NAME:
                return collection.index(item) + 1

    def find_target_data(self, ind1, ind2):
        locator = (By.XPATH, f"//div[@role='row'][{ind1}]/span[@role='cell'][{ind2}]")
        text = self.find_element(locator).text
        return text

    def get_data_to_compare(self):
        text = self.find_element(LABEL_TO_COMPARE).text
        return text
