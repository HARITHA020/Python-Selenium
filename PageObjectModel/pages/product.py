from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class ProductPage(BasePage):

    PRODUCT_LINK = (By.LINK_TEXT, "HP LP3065")

    ADD_TO_CART = (
        By.ID,
        "button-cart"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".alert.alert-success"
    )

    def click_product_link(self):
        self.click(self.PRODUCT_LINK)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)