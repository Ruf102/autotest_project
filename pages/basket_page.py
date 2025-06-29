from autotest_project.pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty_page(self):
        self.should_be_basket_url()
        self.should_be_basket_empty_message()
        self.should_be_basket_empty()

    def should_be_basket_url(self):
        assert "/basket/" in self.browser.current_url, "URL не содержит /basket/"
    def should_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.MASSAGE_EMPTY_BASKET)

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)



