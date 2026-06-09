import pytest
import readconfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup_and_teardown")
class TestDemoblaze:
    def test_purchase_laptop(self):
        username = readconfig.get_config("login credential", "uname")
        password = readconfig.get_config("login credential", "upass")
        self.driver.find_element(By.ID, "login2").click()
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        logout = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "logout2")))
        assert logout.is_displayed()
        print("Login Successful")
        self.driver.find_element(By.LINK_TEXT, "Laptops").click()
        laptop_name = readconfig.get_config("product", "laptop")
        laptop = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, laptop_name)))
        laptop.click()
        title = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='name']")))
        print("Product :", title.text)
        price = self.driver.find_element(By.XPATH, "//h3[@class='price-container']")
        print("Price :", price.text)
        self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        print(alert.text)
        alert.accept()
        self.driver.find_element(By.ID, "cartur").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))).click()
        self.driver.find_element(By.ID, "name").send_keys(readconfig.get_config("order details", "name"))
        self.driver.find_element(By.ID, "country").send_keys(readconfig.get_config("order details", "country"))
        self.driver.find_element(By.ID, "city").send_keys(readconfig.get_config("order details", "city"))
        self.driver.find_element(By.ID, "card").send_keys(readconfig.get_config("order details", "card"))
        self.driver.find_element(By.ID, "month").send_keys(readconfig.get_config("order details", "month"))
        self.driver.find_element(By.ID, "year").send_keys(readconfig.get_config("order details", "year"))
        self.driver.find_element(By.XPATH, "//button[text()='Purchase']").click()
        success = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sweet-alert h2")))
        assert success.text == "Thank you for your purchase!"
        print(success.text)