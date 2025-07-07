import time
from faker import Faker
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.product_page import BasePage
import pytest

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = Faker().email()
        page.register_new_user(email, "1234567890Test")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page = ProductPage(browser, browser.current_url)
        page.should_not_be_success_message()  # Проверяем, что при открытии страницы нет сообщения об успешном добавлении товара

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page = ProductPage(browser, browser.current_url)
        page.should_be_product_page()  # проверяем добавление товара в корзину, сверяем название и цену товара в сообщении об добавлении


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)                   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                         # открываем страницу
    page = ProductPage(browser, browser.current_url)
    page.should_be_product_page()                       # проверяем добавление товара в корзину, сверяем название и цену товара в сообщении об добавлении

@pytest.mark.parametrize('link', [
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/", marks=pytest.mark.skip)])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page = ProductPage(browser, browser.current_url)
    page.should_be_add_product()                        # Добавляем товар в корзину
    page.should_not_be_success_message()                # Проверяем, что нет сообщения об успехе

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page = ProductPage(browser, browser.current_url)
    page.should_not_be_success_message()                # Проверяем, что при открытии страницы нет сообщения об успешном добавлении товара

@pytest.mark.parametrize('link', [
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/", marks=pytest.mark.skip)])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page = ProductPage(browser, browser.current_url)
    page.should_be_add_product()                        # Добавляем товар в корзину
    page.should_be_success_message_disappeared()        # Проверяем, что сообщение исчезло через определенное время

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()                         # Проверяем, что отображается кнопка перехода в авторизацию

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()                             # Проверка открытия формы авторизации со страницы каталога

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()                                       # Открывает страницу с товарами
    page.should_be_cart_button()                      # Проверяем присутствие кнопки "Корзина"
    page.go_to_cart_page()                            # Переходим в корзину
    page = BasketPage(browser, browser.current_url)   # Создаем объект корзина
    page.should_be_basket_empty_page()                # Выполняем проверку пустой корзины