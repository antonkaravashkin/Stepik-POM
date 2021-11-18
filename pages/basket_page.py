from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_busket_message(self):        
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Element is not here"


    def should_be_empty_busket(self):
        assert self.is_not_element_present(*BasketPageLocators.POSITION_IN_BASKET), "It's not empty at all"
