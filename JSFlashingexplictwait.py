from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

def flash_element(element):
    default_color = element.value_of_css_property("background-color")

    for i in range(5):
        driver.execute_script("arguments[0].style.background='red'", element)
        driver.execute_script(f"arguments[0].style.background='{default_color}'", element)

def element_border(element):
    driver.execute_script("arguments[0].style.border='4px solid red'", element)

login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='submit']")))

flash_element(login_button)
element_border(login_button)

driver.quit()