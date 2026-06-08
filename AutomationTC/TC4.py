import time
from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
loginlink=driver.find_element(By.CSS_SELECTOR,"a[href='/login']").click()
time.sleep(5)
loginemail=driver.find_element(By.CSS_SELECTOR,"input[data-qa='login-email']")
loginemail.send_keys("haritha31@gmail.com")
print("the user email:",loginemail.get_attribute("value"))
loginpass=driver.find_element(By.CSS_SELECTOR,"input[placeholder='Password']")
loginpass.send_keys("haritha@20")
print("the user password:",loginpass.get_attribute("value"))
loginbtn=driver.find_element(By.CSS_SELECTOR,"button[data-qa='login-button']")
loginbtn.click()
username=driver.find_element(By.CSS_SELECTOR,"ul.nav.navbar-nav li a b")
username.is_displayed()
print("the loogged user name:",username.text)
logout=driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav']/li[4]").click()
logintext=driver.find_element(By.XPATH,"//div[@class='login-form']/h2")
print("is login text diaplyed:",logintext.is_displayed())
driver.close()






