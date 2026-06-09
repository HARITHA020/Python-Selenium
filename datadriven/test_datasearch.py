import pytest
from selenium.webdriver.common.by import By
import readconfig

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_valid_product(self):
        val=readconfig.get_config("search term","validterm")
        self.driver.find_element(By.NAME, "search").send_keys(val)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()


    def test_invalid_product(self):
        val=readconfig.get_config("search term","invalidterm")
        self.driver.find_element(By.NAME, "search").send_keys(val)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        message = self.driver.find_element(
            By.XPATH, "//p[contains(text(),'There is no product')]"
        ).text
        assert "no product" in message.lower()


    def test_noproduct(self):
        val=readconfig.get_config("search term","noproduct")
        self.driver.find_element(By.NAME, "search").send_keys(val)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        assert "Search" in self.driver.title