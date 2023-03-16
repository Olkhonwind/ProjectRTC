# python -m pytest -v --driver Chrome --driver-path c:\chromedriver/chromedriver.exe tests/test_auth_page.py
import time
import pytest
from pages.auth_page import AuthPage, ChangePass, RegPage
from settings import url_base_page, url_change_page, invalid_name, valid_email_or_phone, valid_password, \
    valid_first_name, valid_last_name, invalid_email_or_phone, invalid_password, \
    random_int, first_name_en, special_chars, russian_chars

class TestAuthPage():
    # Тест №RTC-001
    def test_login_form_opens(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.login_form_opens()

    # Тест №RTC-002
    def test_location_slogan_and_support_info(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.location_slogan_and_support_info()

    # Тест №RTC-003
    def test_location_authentication_selection_menu(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.location_authentication_selection_menu()

    # Тест RTC-004
    def test_default_authorization(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.default_authorization()

    # Тест №RTC-005
    def test_auto_change_authentication_tab(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.auto_change_authentication_tab()

    # Тест №RTC-006
    def test_go_to_the_password_recovery_form(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.go_to_the_password_recovery_form()

    # Тест №RTC-007
    def test_go_to_the_registration_form(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.go_to_the_registration_form()

    # Тест №RTC-008
    def test_authorization_with_empty_fields(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.authorization_with_empty_fields()


class TestChangePass():

    # Тест №RTC-009
    def test_password_recovery_check_with_valid_email(self, browser):
        change_pass_page = ChangePass(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.password_recovery_check_with_valid_email()

    # Тест №RTC-010
    def test_password_recovery_without_code_from_picture(self, browser):
        change_pass_page = ChangePass(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.password_recovery_without_code_from_picture()

    # Тест №RTC-011
    def test_back_button(self, browser):
        change_pass_page = ChangePass(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.back_button()


class TestRegPage():

    # Тест №RTC-012
    @pytest.mark.parametrize('input_text', valid_email_or_phone)
    def test_valid_email_or_phone_data_entry_check(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.valid_email_or_phone_data_entry_check(input_text)

    # Тест №RTC-013
    @pytest.mark.parametrize('input_text', invalid_email_or_phone)
    def test_invalid_email_or_phone_data_entry_check(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.invalid_email_or_phone_data_entry_check(input_text)

    # Тест №RTC-014
    @pytest.mark.parametrize('input_text', valid_password)
    def test_valid_password_check(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.valid_password_check(input_text)

    # Тест №RTC-015
    @pytest.mark.parametrize('input_text', invalid_password)
    def test_invalid_password_check(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.invalid_password_check(input_text)

    # Тест №RTC-016
    @pytest.mark.parametrize('first_name', valid_first_name)
    @pytest.mark.parametrize('last_name', valid_last_name)
    @pytest.mark.parametrize('email_phone', valid_email_or_phone)
    @pytest.mark.parametrize('password', valid_password)
    def test_registration_validation_with_valid_data(self, browser, first_name, last_name, email_phone, password):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.registration_validation_with_valid_data(first_name, last_name, email_phone, password)

    # Тест №RTC-017
    @pytest.mark.parametrize('first_name', [random_int()])
    @pytest.mark.parametrize('last_name', [first_name_en()])
    @pytest.mark.parametrize('email_phone', [special_chars()])
    @pytest.mark.parametrize('password', [russian_chars()])
    def test_registration_validation_with_invalid_data(self, browser, first_name, last_name, email_phone, password):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.registration_validation_with_invalid_data(first_name, last_name, email_phone, password)

    # Тест №RTC-018
    @pytest.mark.parametrize('input_text', invalid_name)
    def test_entering_invalid_name_data(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.entering_invalid_name_data(input_text)










