from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPageLocators():

    registration_email = (By.CSS_SELECTOR, "#id_registration-email")
    registration_password = (By.CSS_SELECTOR, "#id_registration-password1")
    return_registration_password = (By.CSS_SELECTOR, "#id_registration-password2")

    login_user = (By.CSS_SELECTOR, "#id_login-username")
    password_user = (By.CSS_SELECTOR, "#id_login-password")

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert driver.current_url == 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'

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

