from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
driver = wd.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
assert driver.title=="Automation Exercise" 
print("Home page is visible successfully")
driver.find_element(By.XPATH, "//a[contains(text(),'Test Cases')]").click()
fluent_wait = wdw(driver,timeout=10,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
fluent_element = fluent_wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Test Cases')]")))
print("User navigated to Test Cases page successfully")
driver.quit()
