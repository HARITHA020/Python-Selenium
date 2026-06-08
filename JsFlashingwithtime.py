import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
def flash_element(element):
    default_color = element.value_of_css_property("background-color")
    for i in range(5):
        driver.execute_script("arguments[0].style.background='red'",element)
        time.sleep(0.5)
        driver.execute_script(f"arguments[0].style.background='{default_color}'",element)
        time.sleep(0.5)
def element_border(element):
    driver.execute_script("arguments[0].style.border='4px solid red'",element)
login_button = driver.find_element(By.XPATH,"//input[@type='submit']")
flash_element(login_button)
time.sleep(2)
element_border(login_button)
time.sleep(5)
driver.quit()