import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Utilities import logCreator
@pytest.mark.parametrize("username,password", excelReader.get_data("excelfiles/logindata.xlsx", "login"))
class TestLogin1:
    log=logCreator.log_generator()
    def test_validLogin(self, username, password):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demoblaze.com/")
        self.log.info("login website succesfully")
        wait = WebDriverWait(driver, 10)

        try:
            wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

            wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys(username)
            wait.until(EC.visibility_of_element_located((By.ID, "loginpassword"))).send_keys(password)

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))).click()

            try:
                alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
                text = alert.text
                alert.accept()
                assert text in ["User does not exist.", "Wrong password."]
                return

            except TimeoutException:
                pass 
            logout_btn = wait.until(EC.visibility_of_element_located((By.ID, "logout2")))
            assert logout_btn.is_displayed()

        finally:
            driver.quit()