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
    def test_dynamic_id(self, driver):
        main_page = MainPage(driver)
        main_page.go_dynamic_id()
        dynamic_id_page = DynamicIdPage(driver)
        assert dynamic_id_page.can_click_dynamic_id_button()

    def test_ajax_data(self, driver):
        main_page = MainPage(driver)
        main_page.go_ajax_data()
        ajax_page = AjaxPage(driver)
        ajax_page.click_button()
        assert ajax_page.should_be_text_bellow_button()

    def test_scrollbars(self, driver):
        main_page = MainPage(driver)
        main_page.go_scrollbar()
        scroll_page = ScrollBarPage(driver)
        scroll_page.scroll_to_button()
        assert scroll_page.can_click_button()

    def test_visibility(self, driver):
        main_page = MainPage(driver)
        main_page.go_visibility()
        visibility_page = VisibilityPage(driver)
        visibility_page.press_hide_button()
        assert visibility_page.should_disappear()

    def test_class_attribute(self, driver):
        main_page = MainPage(driver)
        main_page.go_class_atr()
        class_art_page = ClassArtPage(driver)
        class_art_page.press_blue_button()
        alert = driver.switch_to_alert()
        alert_text = alert.text
        alert.accept()
        assert alert_text == "Primary button pressed"
        assert class_art_page.should_find_button()

    def test_client_side_delay(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_client_side()
        client_delay_page = ClientDelayPage(driver)
        client_delay_page.press_button()
        assert client_delay_page.should_be_response_bellow()

    def test_dynamic_table(self, driver):
        main_page = MainPage(driver)
        main_page.go_dynamic_table()
        dynamic_table_page = DynamicTablePage(driver)
        headers_list = dynamic_table_page.get_all_headers()
        names_list = dynamic_table_page.get_all_names_from_table()
        index_name = dynamic_table_page.find_target_row_name_index(names_list)
        index_header = dynamic_table_page.find_target_line_name_index(headers_list)
        target_data = dynamic_table_page.find_target_data(index_name, index_header)
        compare_data = dynamic_table_page.get_data_to_compare()
        assert target_data in compare_data

    def test_sample_app(self, driver):
        main_page = MainPage(driver)
        main_page.go_sample_app()
        samp_app_page = SampleAppPage(driver)
        samp_app_page.send_user_name()
        samp_app_page.send_password()
        samp_app_page.press_login_button()
        assert samp_app_page.should_be_success()

    def test_hidden_layers(self, driver):
        main_page = MainPage(driver)
        main_page.go_hidden_layers()
        hidden_layers_page = HiddenLayersPage(driver)
        hidden_layers_page.press_green_button()
        assert hidden_layers_page.should_be_untouchable()

    def test_click(self, driver):
        main_page = MainPage(driver)
        main_page.go_click()
        click_page = ClickPage(driver)
        click_page.click_bad_button()
        assert click_page.should_be_right_colour()

    def test_verify_text(self, driver):
        main_page = MainPage(driver)
        main_page.go_verify_text()
        verify_page = VerifyPage(driver)
        assert verify_page.should_be_welcome_text()

    def test_mouse_over(self, driver):
        main_page = MainPage(driver)
        main_page.go_mouse_over()
        mouse_page = MouseOverPage(driver)
        mouse_page.click_this_text_n_times()
        assert mouse_page.should_be_correct_counter()

    def test_load_delays(self, driver):
        main_page = MainPage(driver)
        main_page.go_load_delays()
        load_page = LoadDelayPage(driver)
        assert load_page.should_be_button()

    def test_text_input(self, driver):
        main_page = MainPage(driver)
        main_page.go_text_input()
        text_page = TextInputPage(driver)
        text_page.send_keys_in_a_diff_way()
        text_page.submit_new_button_name()
        assert text_page.should_be_new_button_name()

    def test_progress_bar(self, driver):
        main_page = MainPage(driver)
        main_page.go_progress_bar()
        progress_bar_page = ProgressBarPage(driver)
        progress_bar_page.make_75()
        assert progress_bar_page.should_be_progress()

    def test_non_space(self, driver):
        main_page = MainPage(driver)
        main_page.go_non_space()
        non_space_page = NonSpacePage(driver)
        assert non_space_page.should_be_button()
