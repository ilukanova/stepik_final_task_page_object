from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[value='Log In']")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")


