from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
def type_text(element, input_text):
    driver.execute_script("arguments[0].value='"+input_text+"'", element)
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
user_name = driver.find_element(By.XPATH, value="//input[@name='email']")
type_text(user_name, 'test@gmail.com')
driver.quit()