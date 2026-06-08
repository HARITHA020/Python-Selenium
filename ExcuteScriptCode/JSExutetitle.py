import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.co.in")
page_title = str(driver.execute_script("return document.title"))
print(page_title)
page_url = str(driver.execute_script("return document.URL"))
print(page_url)
driver.quit()