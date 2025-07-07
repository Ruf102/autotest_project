from .base_page import BasePage
from .locators import LoginPageLocators

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

    def register_new_user(self, email, password):
        email_registration = self.browser.find_element(*LoginPageLocators.registration_email)
        email_registration.send_keys(email)
        password_registration = self.browser.find_element(*LoginPageLocators.registration_password)
        password_registration.send_keys(password)
        password_registration_return = self.browser.find_element(*LoginPageLocators.return_registration_password)
        password_registration_return.send_keys(password)
        button_registration_submit = self.browser.find_element(*LoginPageLocators.registration_submit)
        button_registration_submit.click()



