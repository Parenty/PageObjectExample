from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    PRODUCT_ROW = (By.CSS_SELECTOR, "basket-items")
    MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
