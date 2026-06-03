import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.co.in")
print(driver.title)
time.sleep(5)
driver.quit()