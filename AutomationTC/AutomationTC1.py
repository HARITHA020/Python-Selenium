from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.maximize_window()
driver.get("https://automationexercise.com/")

driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()

wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys("harithaSR")

driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys("haritha31@gmail.com")

driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()

wait.until(EC.visibility_of_element_located((By.XPATH, "//b[normalize-space()='Enter Account Information']")))

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='id_gender2']"))).click()

driver.find_element(By.ID, "password").send_keys("haritha@20")

driver.find_element(By.ID, "days").click()
driver.find_element(By.CSS_SELECTOR, "#days > option:nth-child(5)").click()

months = driver.find_element(By.ID, "months")
driver.execute_script("arguments[0].scrollIntoView(true);", months)
months.click()

driver.find_element(By.CSS_SELECTOR, "#months > option:nth-child(6)").click()

driver.find_element(By.ID, "years").click()
driver.find_element(By.CSS_SELECTOR, "#years > option:nth-child(6)").click()

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

country = driver.find_element(By.ID, "country")
driver.execute_script("arguments[0].scrollIntoView(true);", country)
country.click()

driver.find_element(By.CSS_SELECTOR, "#country > option:nth-child(1)").click()

state=driver.find_element(By.ID, "state").send_keys("TamilNadu")
city=driver.find_element(By.ID, "city").send_keys("Salem")
zipcode=driver.find_element(By.ID, "zipcode").send_keys("223344")
number=driver.find_element(By.ID, "mobile_number").send_keys("5469874526")

driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']").click()

print("Account Created Successfully")

driver.quit()