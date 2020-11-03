from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_USERNAME), "Login username field is not presented"
        assert self.is_element_present(*MainPageLocators.LOGIN_PASSWORD), "Login password field is not presented"
        assert self.is_element_present(*MainPageLocators.LOGIN_BUTTON), "Login button is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTRATION_EMAIL), "Registration email field is not presented"
        assert self.is_element_present(*MainPageLocators.REGISTRATION_PASSWORD1), "Registration password1 field is not presented"
        assert self.is_element_present(*MainPageLocators.REGISTRATION_PASSWORD2), "Registration password2 field is not presented"
        assert self.is_element_present(*MainPageLocators.REGISTRATION_BUTTON), "Registration button is not presented"