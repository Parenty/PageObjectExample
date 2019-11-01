from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "'login' is not in url"

    def should_be_login_form(self):
        assert self.browser.find_element(By.CSS_SELECTOR, '#login_form')

    def should_be_register_form(self):
        assert self.browser.find_element(By.CSS_SELECTOR, '#register_form')

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT_BUTTON).click()
