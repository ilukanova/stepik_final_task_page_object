from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[value='Log In']")
    REG_EMAIL = (By.ID, "id_registration-email")
    REG_PASSWORD = (By.ID, "id_registration-password1")
    REG_PASSWORD_REPEAT = (By.ID, "id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    MESSAGE_PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages > div.alert:first-child > div.alertinner")
    MESSAGE_PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, "#messages > div.alert:nth-child(3) > div.alertinner > p")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    PRODUCTS_IN_BASKET = (By.ID, "basket_formset")
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
