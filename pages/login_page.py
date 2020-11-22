from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login username field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), \
            "Registration email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD), \
            "Registration password1 field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_REPEAT), \
            "Registration password2 field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), \
            "Registration button is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
