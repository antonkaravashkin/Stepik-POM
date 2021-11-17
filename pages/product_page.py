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
        if goods_name in goods_matched:
            assert True, "Names does not compare!"
        else:
            assert False
            
    
