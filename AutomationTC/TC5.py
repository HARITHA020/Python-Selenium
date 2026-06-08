import time
from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
loginlink=driver.find_element(By.CSS_SELECTOR,"a[href='/login']").click()
time.sleep(5)
sigupname=driver.find_element(By.XPATH,"//div[@class='signup-form']/form/input[2]")
sigupname.send_keys("haritha11@gmail.com")
siguppass=driver.find_element(By.XPATH,"//div[@class='signup-form']/form/input[3]")
siguppass.send_keys("haritha@20")
sigupbtn=driver.find_element(By.XPATH,"//div[@class='signup-form']/form/button")
driver.execute_script("arguments[0].click();", sigupbtn)
errmsg=driver.find_element(By.XPATH,"//div[@class='signup-form']/form/p")
assert errmsg.text == "Email Address already exist!"
print("Assertion Passed")
driver.close()
