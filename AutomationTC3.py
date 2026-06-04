import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationexercise.com/")

driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
time.sleep(2)
loginemail = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']")
loginemail.send_keys("haritha25@gmail.com")
loginpass = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
loginpass.send_keys("haritha@20")
driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()
errormsg = driver.find_element(By.XPATH,"//p[contains(text(),'Your email or password is incorrect!')]")
print("Error Message:", errormsg.text)
driver.save_screenshot("invalid_login.png")
assert errormsg.text == "Your email or password is incorrect!", "Invalid login test failed"
print("Invalid login")
driver.quit()