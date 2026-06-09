import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import readconfig

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_validlogin(self):
        self.driver.find_element(By.ID, "login2").click()
        username = readconfig.get_config("login credential", "uname")
        password = readconfig.get_config("login credential", "upass")
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        logout = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "logout2")))
        assert logout.is_displayed()
        userlogged=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#nameofuser")))
        print("the logged username:",userlogged.text)
        
    def test_invalidlogin(self):
        self.driver.find_element(By.ID, "login2").click()
        username = readconfig.get_config("invalid credentials", "uname")
        password = readconfig.get_config("invalid credentials", "upass")
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert alert.text == "Wrong password."
        alert.accept()
        
    