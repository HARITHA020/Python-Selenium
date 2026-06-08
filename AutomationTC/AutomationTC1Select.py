from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.maximize_window()
driver.get("https://automationexercise.com/")

driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()

wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys("harithaSR")

driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys("haritha32@gmail.com")

driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()

wait.until(EC.visibility_of_element_located((By.XPATH, "//b[normalize-space()='Enter Account Information']")))

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='id_gender2']"))).click()

driver.find_element(By.ID, "password").send_keys("haritha@20")

Select(driver.find_element(By.ID, "days")).select_by_visible_text("4")
Select(driver.find_element(By.ID, "months")).select_by_visible_text("May")
Select(driver.find_element(By.ID, "years")).select_by_visible_text("2000")

firstname = driver.find_element(By.ID, "first_name")
firstname.send_keys("haritha")
print("First Name:", firstname.get_attribute("value"))

lastname = driver.find_element(By.ID, "last_name")
lastname.send_keys("D")
print("Last Name:", lastname.get_attribute("value"))

company = driver.find_element(By.ID, "company")
company.send_keys("ZZZZ")
print("Company:", company.get_attribute("value"))

address = driver.find_element(By.ID, "address1")
address.send_keys("YYYY")
print("Address:", address.get_attribute("value"))

Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")

driver.find_element(By.ID, "state").send_keys("TamilNadu")
driver.find_element(By.ID, "city").send_keys("Salem")
driver.find_element(By.ID, "zipcode").send_keys("223344")
driver.find_element(By.ID, "mobile_number").send_keys("5469874526")

driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']").click()

account_msg = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//b[normalize-space()='Account Created!']")
    )
)

print(account_msg.text)

assert account_msg.text == "ACCOUNT CREATED!"

print("Account Created Successfully")

driver.quit()