from .base_page import BasePage
from .locators import ProductPageLocators
import pytest


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_add_product()
        self.should_be_add_in_cart()
        self.should_be_price_in_cart()

    def should_be_add_product(self):
        add_but = self.browser.find_element(*ProductPageLocators.add_product_button)
        assert add_but, "Не найдена кнопка добавления товара"
        add_but.click()

    def should_be_add_in_cart(self):
        assert (self.browser.find_element(*ProductPageLocators.product_name).text ==
                self.browser.find_element(*ProductPageLocators.massage_for_add_product).text), "Название товара не совпадает с названием товара добавленного в корзину"

    def should_be_price_in_cart(self):
        assert (self.browser.find_element(*ProductPageLocators.product_price).text in
                self.browser.find_element(*ProductPageLocators.massage_sale_price).text), "Цена товара не совпадает, с ценой товара добавленного в корзину"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.massage_for_add_product), "Сообщение об успешном добавлении товара не исчезло, через определенное время"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.massage_for_add_product), "Сообщение об успешном выполнении отображается, но не должно"








