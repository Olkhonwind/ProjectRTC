from settings import valid_email, valid_phone, random_int
from .base_page import BasePage
from .locators import BaseLocators, AuthPageLocators, EmailConfirmLocators, ChangePassLocators, \
    RegisLocators


class AuthPage(BasePage):
    # для проверки перехода на форму авторизации
    def login_form_opens(self):
        assert self.is_element_present(AuthPageLocators.AUTH_HEADING)
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth" in self.browser.current_url, \
            "url do not match"

    # для проверки расположения логотипа и слогана
    def location_slogan_and_support_info(self):
        assert self.is_element_present(AuthPageLocators.AUTH_LOGO), "element not found"
        assert self.is_element_present(AuthPageLocators.AUTH_SLOGAN), "element not found"

    # для проверки расположения меню выбора типа аутентификации
    def location_authentication_selection_menu(self):
        assert self.is_element_present(AuthPageLocators.AUTH_TAB_MENU), "element not found"

    # для проверки типа аутентификации по умолчанию
    def default_authorization(self):
        assert self.is_element_present(AuthPageLocators.AUTH_USERNAME_INPUT_PLACEHOLDER_TELEPHONE), \
            "element not found"

    # для проверки автоматического изменения типа аутентификации
    def auto_change_authentication_tab(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(valid_email())
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(AuthPageLocators.AUTH_USERNAME_INPUT_ACTIV_EMAIL), "element not found"

    # для проверки ссылки перехода на форму восстановления пароля
    def go_to_the_password_recovery_form(self):
        self.find_element(AuthPageLocators.AUTH_FORGOT_PASSWORD_LINK).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.browser.current_url, "url do not match"
        assert self.is_element_present(ChangePassLocators.CHANGE_PASS_HEADING), "element not found"

    # для проверки ссылки на форму регистрации
    def go_to_the_registration_form(self):
        self.find_element(AuthPageLocators.AUTH_REGISTER_LINK).click()
        assert self.is_element_present(RegisLocators.REG_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration" \
               in self.browser.current_url, "url do not match"

    # для проверки авторизации с пустыми полями
    def authorization_with_empty_fields(self):
        self.find_element(AuthPageLocators.AUTH_TAB_PHONE).click()
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert self.is_element_present(AuthPageLocators.AUTH_ERROR_ENTER_PHONE_NUMBER), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth" in self.browser.current_url, \
            "url do not match"

class ChangePass(BasePage):
    # для проверки формы "Восстановление пароля" на ввод действительного email
    def password_recovery_check_with_valid_email(self):
        self.find_element(ChangePassLocators.CHANGE_PASS_TAB_MAIL).click()
        username_input = self.find_element(ChangePassLocators.CHANGE_PASS_USERNAME_INPUT)
        email = valid_email()
        username_input.send_keys(email)
        self.find_element(BaseLocators.BODY).click()
        element = self.find_element(ChangePassLocators.CHANGE_PASS_USERNAME_INPUT_VALUE)
        value = element.get_attribute("value")
        assert email == value, "email do not match"

    # для проверки на странице формы "Восстановление пароля" кнопки "Вернуться назад"
    def back_button(self):
        self.find_element(ChangePassLocators.CHANGE_PASS_GO_BACK_BUTTON).click()
        assert self.is_element_present(AuthPageLocators.AUTH_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate" in self.browser.current_url, \
            "url do not match"

    # для проверки формы "Восстановление пароля" без ввода символов с картинки
    def password_recovery_without_code_from_picture(self):
        self.find_element(ChangePassLocators.CHANGE_PASS_TAB_MAIL).click()
        self.find_element(ChangePassLocators.CHANGE_PASS_USERNAME_INPUT).send_keys(valid_email())
        self.find_element(ChangePassLocators.CHANGE_PASS_CONTINUE_BUTTON).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.browser.current_url, "url do not match"
        assert self.is_element_present(ChangePassLocators.CHANGE_PASS_ERROR_INVALID_USERNAME_OR_TEXT), \
            "element not found"

class RegPage(BasePage):
    # Проверка формы "Регистрация" на ввод действительных e-mail или мобильного телефона
    def valid_email_or_phone_data_entry_check(self, input_text):
        self.find_element(RegisLocators.REG_EMAIL_PHONE_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        element = self.find_element(RegisLocators.REG_EMAIL_PHONE_INPUT_VALUE)
        value = element.get_attribute("value")
        assert input_text == value, "email or phone do not match"
        assert self.is_not_element_present(RegisLocators.REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT), "element found"

    # Проверка формы "Регистрация" на ввод недействительных e-mail или мобильного телефона
    def invalid_email_or_phone_data_entry_check(self, input_text):
        self.find_element(RegisLocators.REG_EMAIL_PHONE_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegisLocators.REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT), "element not found"

    # Проверка формы "Регистрация" на ввод действительного пароля
    def valid_password_check(self, input_text):
        self.find_element(RegisLocators.REG_PASSWORD_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_not_element_present(RegisLocators.REG_ERROR_INVALID_PASSWORD_INPUT), "element found"

    # Проверка формы "Регистрация" на ввод недействительного пароля
    def invalid_password_check(self, input_text):
        self.find_element(RegisLocators.REG_PASSWORD_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegisLocators.REG_ERROR_INVALID_PASSWORD_INPUT), "element not found"

    # Проверка регистрации с действительными данными
    def registration_validation_with_valid_data(self, first_name, last_name, email_phone, password):
        self.find_element(RegisLocators.REG_FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(RegisLocators.REG_LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(RegisLocators.REG_EMAIL_PHONE_INPUT).send_keys(email_phone)
        self.find_element(RegisLocators.REG_PASSWORD_INPUT).send_keys(password)
        self.find_element(RegisLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.find_element(RegisLocators.REG_ENTER_BUTTON).click()
        assert self.is_element_present(EmailConfirmLocators.EMAIL_CONF_HEADING), "element not found"

    # Проверка регистрации с недействительными данными
    def registration_validation_with_invalid_data(self, first_name, last_name, email_phone, password):
        self.find_element(RegisLocators.REG_FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(RegisLocators.REG_LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(RegisLocators.REG_EMAIL_PHONE_INPUT).send_keys(email_phone)
        self.find_element(RegisLocators.REG_PASSWORD_INPUT).send_keys(password)
        self.find_element(RegisLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.find_element(RegisLocators.REG_ENTER_BUTTON).click()
        assert self.is_not_element_present(EmailConfirmLocators.EMAIL_CONF_HEADING), "element found"

    # Проверка формы "Регистрация" на ввод недействительных данных в поле "Имя"
    def entering_invalid_name_data(self, input_text):
        self.find_element(RegisLocators.REG_FIRST_NAME_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegisLocators.REG_ERROR_FIRST_NAME_INPUT), "element not found"
