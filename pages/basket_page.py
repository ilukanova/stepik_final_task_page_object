from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Basket is not empty, but should be"

    def should_be_message_basket_is_empty(self):
        text_basket_is_empty = "Your basket is empty."
        message_basket_is_empty = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY).text
        assert text_basket_is_empty in message_basket_is_empty, \
            "Message - 'Basket is not empty' is not presented, but should be"
