import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.co.in")
print("Title:", driver.title)
searchbox = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
print("is enabled search  button:",searchbox.is_enabled())
searchbox.send_keys("Selenium Python")
time.sleep(2)
search_btn = driver.find_element(By.NAME, "btnK")
print("is enabled button:",search_btn.is_enabled())
time.sleep(5)
driver.quit()