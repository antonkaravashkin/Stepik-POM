from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        substring = self.browser.current_url
        if "login" in substring:
            assert True, "Login string is not presented in link"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login FORM is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_ADRESS), "Login EMAIL_FIELD is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), "Login PASSWORD_FIELD is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login BUTTON is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration FORM is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_ADRESS), "Registration EMAIL_FIELD is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD), "Registration PASSWORD_FIELD is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD), "Registration CONFIRM_PASS_FIELD is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_BUTTON), "Registration CONFIRM_BUTTON is not presented"