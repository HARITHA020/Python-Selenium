import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_valid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("HP")
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()


    def test_invalid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("XYZ123")
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        message = self.driver.find_element(
            By.XPATH, "//p[contains(text(),'There is no product')]"
        ).text
        assert "no product" in message.lower()


    def test_noproduct(self):
        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        assert "Search" in self.driver.title