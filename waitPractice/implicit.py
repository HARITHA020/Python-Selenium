from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://automationexercise.com/")
assert driver.title=="Automation Exercise" 
print("Home page is visible successfully")
driver.find_element(By.XPATH, "//a[contains(text(),'Test Cases')]").click()
print("User navigated to Test Cases page successfully")
driver.quit()