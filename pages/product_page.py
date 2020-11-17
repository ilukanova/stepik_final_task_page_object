from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()
        self.solve_quiz_and_get_code()
        self.should_be_message_adding_to_basket(self.get_product_name())
        self.should_be_message_with_product_price(self.get_product_price())

    def should_be_message_adding_to_basket(self, product_name):
        message_adding_to_basket = self.browser.find_element(
            *ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET).text
        print(message_adding_to_basket)
        assert message_adding_to_basket == f"{product_name} has been added to your basket.",\
            "Wrong message adding to basket"

    def should_be_message_with_product_price(self, product_price):
        message_with_product_price = self.browser.find_element(
            *ProductPageLocators.MESSAGE_PRODUCT_PRICE_BASKET).text
        print(message_with_product_price)
        assert message_with_product_price == f"Your basket total is now {product_price}",\
            "Wrong message with product price"

    def get_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name of product is not found"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price of product is not found"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), \
            "Success message is not disappeared, but should be"
