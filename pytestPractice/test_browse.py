import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('search',[("selenium"),("python")])
def test_google_search(search):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://google.co.in/")
    driver.find_element(By.NAME,value="q").send_keys(search)
    time.sleep(6)
    driver.find_element(By.CLASS_NAME,value='gNO89b').click()
    time.sleep(6)
    driver.quit()