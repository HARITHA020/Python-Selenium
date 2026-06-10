from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class LoginPage(BasePage):

    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    def enter_form_details(self, username, password):
        self.type(self.EMAIL, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)