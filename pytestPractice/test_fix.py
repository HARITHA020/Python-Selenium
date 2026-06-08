import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setup_and_teardown():
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()

def test_valid(test_setup_and_teardown):
    driver.find_element(By.NAME,value='search').send_keys("HP")
    driver.find_element(By.XPATH,"value='//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT,value="HP LP3065").is_displayed()
    
def test_invalid(test_setup_and_teardown):
    driver.find_element(By.NAME,value='search').send_keys("Honda")
    driver.find_element(By.XPATH,"value='//button[contains(@class,'btn-default')]").click()
    expexted="there is no product"
    assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expexted)

def test_noproduct(test_setup_and_teardown):
    driver.find_element(By.NAME,value='search').send_keys("")
    driver.find_element(By.XPATH,"value='//button[contains(@class,'btn-default')]").click()
    expexted="there is no product"
    assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expexted)
    