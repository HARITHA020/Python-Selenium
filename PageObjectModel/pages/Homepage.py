from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class HomePage(BasePage):

    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='btn btn-default btn-lg']")

    def enter_product(self, product):
        self.type(self.SEARCH_BOX, product)

    def click_search(self):
        self.click(self.SEARCH_BUTTON)