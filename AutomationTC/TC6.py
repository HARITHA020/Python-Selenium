from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
contact=driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav']/li[8]")
contact.click()
text=driver.find_element(By.XPATH,"//div[@class='contact-form']/h2")
print("is text is displayed:",text.is_displayed())
name=driver.find_element(By.XPATH,"//form[@id='contact-us-form']/div[1]/input")
name.send_keys("haritha")
email=driver.find_element(By.XPATH,"//form[@id='contact-us-form']/div[2]/input")
email.send_keys("haritha11@gmail.com")
submitbtn=driver.find_element(By.XPATH,"//form[@id='contact-us-form']/div[6]/input")
submitbtn.click()
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
print("Alert text:", alert.text)
alert.accept()
print("Alert accepted successfully")