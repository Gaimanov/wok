from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import faker
import time


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTER_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_field.send_keys(email)

        pw_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        pw_field.send_keys(password)

        confirm_pw = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_pw.send_keys(password)

        btn_submit = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        btn_submit.click()


