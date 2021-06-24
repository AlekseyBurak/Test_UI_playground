import allure

from pages.main_page import MainPage
from pages.dynamic_id_page import DynamicIdPage
from pages.ajax_page import AjaxPage
from pages.scrollbar_page import ScrollBarPage
from pages.visibility_page import VisibilityPage
from pages.class_atr_page import ClassArtPage
from pages.cliant_delay_page import ClientDelayPage
from pages.dynamic_table_page import DynamicTablePage
from pages.sample_app_page import SampleAppPage
from pages.hidden_layers_page import HiddenLayersPage
from pages.click_page import ClickPage
from pages.verify_page import VerifyPage
from pages.mouse_over_page import MouseOverPage
from pages.load_delay_page import LoadDelayPage
from pages.text_input_page import TextInputPage
from pages.progress_bar_page import ProgressBarPage
from pages.non_space_page import NonSpacePage


class TestUiPlayground:
    @allure.story('Testing page with dynamic ID button')
    def test_dynamic_id(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_dynamic_id()
        with allure.step('Try to click bad button'):
            dynamic_id_page = DynamicIdPage(driver)
            assert dynamic_id_page.can_click_dynamic_id_button()

    @allure.story('Testing page with ajax data')
    def test_ajax_data(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_ajax_data()
        with allure.step('Try to click button and compare text'):
            ajax_page = AjaxPage(driver)
            ajax_page.click_button()
            assert ajax_page.should_be_text_bellow_button()

    @allure.story('Testing page with scrollbars')
    def test_scrollbars(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_scrollbar()
        with allure.step('Try to scroll and click'):
            scroll_page = ScrollBarPage(driver)
            scroll_page.scroll_to_button()
            assert scroll_page.can_click_button()

    @allure.story('Testing page with invisible buttons')
    def test_visibility(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_visibility()
        with allure.step('Press button and the others will gone'):
            visibility_page = VisibilityPage(driver)
            visibility_page.press_hide_button()
            assert visibility_page.should_disappear()

    @allure.story('Testing page with some button and alert')
    def test_class_attribute(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_class_atr()
        with allure.step('Click button, switch to alert, assert'):
            class_art_page = ClassArtPage(driver)
            class_art_page.press_blue_button()
            alert = driver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
            assert alert_text == "Primary button pressed"
            assert class_art_page.should_find_button()

    @allure.story('Testing page with client delay')
    def test_client_side_delay(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_to_client_side()
        with allure.step('We wait'):
            client_delay_page = ClientDelayPage(driver)
            client_delay_page.press_button()
            assert client_delay_page.should_be_response_bellow()

    @allure.story('Testing page with dynamic table')
    def test_dynamic_table(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_dynamic_table()
        with allure.step('Have some mess with tables'):
            dynamic_table_page = DynamicTablePage(driver)
            headers_list = dynamic_table_page.get_all_headers()
            names_list = dynamic_table_page.get_all_names_from_table()
            index_name = dynamic_table_page.find_target_row_name_index(names_list)
            index_header = dynamic_table_page.find_target_line_name_index(headers_list)
            target_data = dynamic_table_page.find_target_data(index_name, index_header)
            compare_data = dynamic_table_page.get_data_to_compare()
        assert target_data in compare_data

    @allure.story('Testing page with input fields')
    def test_sample_app(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_sample_app()
        with allure.step('Input your personal data and login'):
            samp_app_page = SampleAppPage(driver)
            samp_app_page.send_user_name()
            samp_app_page.send_password()
            samp_app_page.press_login_button()
            assert samp_app_page.should_be_success()

    @allure.story('Testing page with hidden layers')
    def test_hidden_layers(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_hidden_layers()
        with allure.step('Can`t touch this'):
            hidden_layers_page = HiddenLayersPage(driver)
            hidden_layers_page.press_green_button()
            assert hidden_layers_page.should_be_untouchable()

    @allure.story('Testing page with 50 shades of click')
    def test_click(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_click()
        with allure.step('This button is bad. Smack it'):
            click_page = ClickPage(driver)
            click_page.click_bad_button()
            assert click_page.should_be_right_colour()

    @allure.story('Testing page where we verifying text')
    def test_verify_text(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_verify_text()
        with allure.step('Read html'):
            verify_page = VerifyPage(driver)
            assert verify_page.should_be_welcome_text()

    @allure.story('Testing page with mouse on vacation')
    def test_mouse_over(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_mouse_over()
        with allure.step('I literally hate this task'):
            mouse_page = MouseOverPage(driver)
            mouse_page.click_this_text_n_times()
            assert mouse_page.should_be_correct_counter()

    @allure.story('Testing page with load delays')
    def test_load_delays(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_load_delays()
        with allure.step('we wait...again'):
            load_page = LoadDelayPage(driver)
            assert load_page.should_be_button()

    @allure.story('Testing page with bad input fields')
    def test_text_input(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_text_input()
        with allure.step('send your personal data like a pro'):
            text_page = TextInputPage(driver)
            text_page.send_keys_in_a_diff_way()
            text_page.submit_new_button_name()
            assert text_page.should_be_new_button_name()

    @allure.story('Testing page with progress bar')
    def test_progress_bar(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_progress_bar()
        with allure.step('it is over 9000'):
            progress_bar_page = ProgressBarPage(driver)
            progress_bar_page.make_75()
            assert progress_bar_page.should_be_progress()

    @allure.story('Testing page with special space')
    def test_non_space(self, driver):
        with allure.step('Go to main page'):
            main_page = MainPage(driver)
            main_page.go_non_space()
        with allure.step('there isn`t space you are looking for'):
            non_space_page = NonSpacePage(driver)
            assert non_space_page.should_be_button()
