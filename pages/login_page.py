from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.login_user), "не найдено поле ввода логина в форме авторизации"
        assert self.is_element_present(*LoginPageLocators.password_user), "не найдено поле ввода пароля в форме авторизации"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.registration_email), "не найдено поле ввода адреса email в форме регистрации"
        assert self.is_element_present(
            *LoginPageLocators.registration_password), "не найдено поле ввода пароля в форме регистрации"
        assert self.is_element_present(
            *LoginPageLocators.return_registration_password), "не найдено поле повторного ввода пароля  в форме регистрации"

