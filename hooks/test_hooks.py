from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check

def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo")

def teardown_function(function):
    global driver
    driver.quit()

def test_valid_product():
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()

    check.is_true(driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed(),"Product not displayed")

    check.equal(driver.title, "Search", "Title mismatch")


def test_invalid_product():
    driver.find_element(By.NAME, "search").send_keys("XYZ123")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()

    message = driver.find_element(By.XPATH,"//p[contains(text(),'There is no product')]").text
    check.is_in("no product", message.lower())
    check.equal(driver.title, "Search", "Title mismatch")
def test_noproduct():
    driver.find_element(By.NAME, "search").send_keys("")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    check.is_in("Search", driver.title)
    check.is_true(driver.current_url.endswith("search"))