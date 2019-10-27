from selenium.webdriver.common.by import By

from .base_page import BasePage


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