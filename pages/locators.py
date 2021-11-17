from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_ADRESS = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    FORGOT_PASSWORD = (By.LINK_TEXT, "Я забыл пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")

    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_ADRESS = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "id_registration-password2")
    REGISTRATION_CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")