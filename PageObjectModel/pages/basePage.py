from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator, text):
        element = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator):
        return WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    def get_text(self, locator):
        return WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(locator)
        ).text