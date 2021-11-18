from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

#class MainPageLocators():
#    pass
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_ADRESS = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    FORGOT_PASSWORD = (By.LINK_TEXT, "Я забыл пароль")
    LOGIN_BUTTON = (By.NAME, "login_submit")

    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_ADRESS = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_CONFIRM_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_CART = (By.XPATH, "//form/button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    GOODS_ADDED_MESSAGE = (By.XPATH, "//div[@id='messages']//div[1]//div[1]/strong")
    GOODS_NAME = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] h1" )
    PRICE_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alertinner')]/p[1]")
    PRICE = (By.XPATH, "//p[contains(@class,'price_color')]")
