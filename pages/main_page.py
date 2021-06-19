from base_page import BasePage
from selenium.webdriver.common.by import By

# LOCATORS
DYNAMIC_ID = (By.XPATH, "//a[@href='/dynamicid']")
AJAX_DATA = (By.XPATH, "//a[@href='/ajax']")
SCROLLBARS = (By.XPATH, "//a[@href='/scrollbars']")
VISIBILITY = (By.XPATH, "//a[@href='/visibility']")
CLASS_ATRIBUTE = (By.XPATH, "//a[@href='/classattr']")
CLIENT_SIDE_DELAY = (By.XPATH, "//a[@href='/clientdelay']")
DYNAMIC_TABLE = (By.XPATH, "//a[@href='/dynamictable']")
SAMPLE_APP = (By.XPATH, "//a[@href='/sampleapp']")
HIDDEN_LAYERS = (By.XPATH, "//a[@href='/hiddenlayers']")
CLICK = (By.XPATH, "//a[@href='/click']")
VERIFY_TEXT = (By.XPATH, "//a[@href='/verifytext']")
MOUSE_OVER = (By.XPATH, "//a[@href='/mouseover']")
LOAD_DELAY = (By.XPATH, "//a[@href='/loaddelay']")
TEXT_INPUT = (By.XPATH, "//a[@href='/textinput']")
PROGRESS_BAR = (By.XPATH, "//a[@href='/progressbar']")
NON_BREAKING_SPACE = (By.XPATH, "//a[@href='/nbsp']")


class MainPage(BasePage):
    def go_dynamic_id(self):
        self.find_element(DYNAMIC_ID).click()

    def go_ajax_data(self):
        self.find_element(AJAX_DATA).click()

    def go_scrollbar(self):
        self.find_element(SCROLLBARS).click()

    def go_visibility(self):
        self.find_element(VISIBILITY).click()

    def go_class_atr(self):
        self.find_element(CLASS_ATRIBUTE).click()

    def go_to_client_side(self):
        self.find_element(CLIENT_SIDE_DELAY).click()

    def go_dynamic_table(self):
        self.find_element(DYNAMIC_TABLE).click()

    def go_sample_app(self):
        self.find_element(SAMPLE_APP).click()

    def go_hidden_layers(self):
        self.find_element(HIDDEN_LAYERS).click()

    def go_click(self):
        self.find_element(CLICK).click()

    def go_verify_text(self):
        self.find_element(VERIFY_TEXT).click()

    def go_mouse_over(self):
        self.find_element(MOUSE_OVER).click()

    def go_load_delays(self):
        self.find_element(LOAD_DELAY).click()

    def go_text_input(self):
        self.find_element(TEXT_INPUT).click()

    def go_progress_bar(self):
        self.find_element(PROGRESS_BAR).click()

    def go_non_space(self):
        self.find_element(NON_BREAKING_SPACE).click()

