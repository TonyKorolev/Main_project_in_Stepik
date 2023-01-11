from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_dissapear_of_products_in_basket_page(self):
        assert self.is_disappeared(*BasketPageLocators.PRODUCT_IN_BASKET_PAGE), \
            "Products are in basket page"
    
    def should_be_basket_is_empty_in_basket_page(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
            "No message basket is empty"