from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("https://automationexercise.com/")
assert driver.title=="Automation Exercise" 
print("Home page is visible successfully")
driver.find_element(By.XPATH, "//a[contains(text(),'Test Cases')]").click()
testcase_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Test Cases')]")))
assert testcase_title.is_displayed()
print("User navigated to Test Cases page successfully")
driver.quit()