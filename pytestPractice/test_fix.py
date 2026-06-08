import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def test_setup_and_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo")
    yield
    driver.quit()


def test_valid_product(test_setup_and_teardown):
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()


def test_invalid_product(test_setup_and_teardown):
    driver.find_element(By.NAME, "search").send_keys("XYZ123")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    message = driver.find_element(By.XPATH, "//p[contains(text(),'There is no product')]").text
    assert "no product" in message.lower()

def test_noproduct(test_setup_and_teardown):

    driver.find_element(By.NAME, "search").send_keys("###INVALID###")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    message = driver.find_element(By.XPATH, "//*[contains(text(),'no product')]").text
    assert "no product" in message.lower()