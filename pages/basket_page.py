from .locators import BasketPageLocators

from .base_page import BasePage


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        self.basket_should_be_empty()
        self.basket_should_be_message_empty()

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_ROW), \
            "Basket is not empty!"

    def basket_should_be_message_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY), \
            "No message about empty basket!"
