import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utilities import excelReader
from utilities import logCreator


@pytest.mark.parametrize(
    "email,password",
    excelReader.get_data("ExcelFiles/loginData.xlsx", "login")
)
class TestTutorialsNinjaLogin:

    log = logCreator.log_generator()

    def test_login(self, email, password):

        driver = webdriver.Chrome()
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)

        try:
            driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
            self.log.info("Opened TutorialsNinja login page")

            wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(email)

            wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']"))).click()

            try:
                warning = wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, ".alert-danger")
                    )
                )
                text = warning.text

                assert "Warning: No match for E-Mail Address and/or Password." in text
                self.log.info("Invalid login verified")
                return

            except TimeoutException:
                pass

            my_account = wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "My Account"))
            )

            assert my_account.is_displayed()
            self.log.info("Login successful")

        finally:
            driver.quit()