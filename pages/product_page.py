from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators


class ProductPage(BasePage):

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET)

    def add_to_basket_product(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
    
    def check_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
            self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_ADDED_TO_BASKET).text, \
                "Products' name are not the same"
    
    def check_price_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text == \
            self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text, \
                "Product's price does't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    
    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is appers"