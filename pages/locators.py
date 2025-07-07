from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-group.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    registration_email = (By.CSS_SELECTOR, "#id_registration-email")
    registration_password = (By.CSS_SELECTOR, "#id_registration-password1")
    return_registration_password = (By.CSS_SELECTOR, "#id_registration-password2")
    login_user = (By.CSS_SELECTOR, "#id_login-username")
    password_user = (By.CSS_SELECTOR, "#id_login-password")
    registration_submit = (By.CSS_SELECTOR, "#register_form > button")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class ProductPageLocators:
    add_product_button = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    product_name = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    product_price = (By.CSS_SELECTOR, "p.price_color")
    product_sale_name = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    massage_for_add_product =  (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    massage_sale_price = (By.XPATH, "//*[@id='messages']/div[3]/div")

class BasketPageLocators:
    MASSAGE_EMPTY_BASKET = (By.ID, "content_inner")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


