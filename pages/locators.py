from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    registration_email = (By.CSS_SELECTOR, "#id_registration-email")
    registration_password = (By.CSS_SELECTOR, "#id_registration-password1")
    return_registration_password = (By.CSS_SELECTOR, "#id_registration-password2")
    login_user = (By.CSS_SELECTOR, "#id_login-username")
    password_user = (By.CSS_SELECTOR, "#id_login-password")

class ProductPageLocators:
    add_product_button = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    product_name = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    product_price = (By.CSS_SELECTOR, "p.price_color")
    product_sale_name = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    massage_for_add_product =  (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    massage_sale_price = (By.XPATH, "//*[@id='messages']/div[3]/div")


