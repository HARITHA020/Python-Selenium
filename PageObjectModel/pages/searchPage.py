from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class SearchPage(BasePage):

    PRODUCT = (By.LINK_TEXT, "HP LP3065")

    def verify_product(self):
        return self.is_displayed(self.PRODUCT)