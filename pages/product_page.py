from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart.click()


    def goods_is_added_to_bucket(self):        
        assert self.is_element_present(*ProductPageLocators.GOODS_ADDED_MESSAGE), "Message missing"


    def goods_name_equal_name(self): 
        goods_matched = self.browser.find_element(*ProductPageLocators.GOODS_ADDED_MESSAGE).text
        goods_name = self.browser.find_element(*ProductPageLocators.GOODS_NAME).text
        assert goods_name == goods_matched, 'No such names'


    def goods_price_mesage(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_SUCCESS_MESSAGE), "Price message missing"


    def goods_equal_prices(self): 
        price_matched = self.browser.find_element(*ProductPageLocators.PRICE_SUCCESS_MESSAGE).text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert price in price_matched, "Prices does not compare!"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.GOODS_ADDED_MESSAGE), "element is on page"


    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.GOODS_ADDED_MESSAGE), "is not dissapeared"