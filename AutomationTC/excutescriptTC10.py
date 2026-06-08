from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://automationexercise.com")
assert "Automation Exercise" in driver.title
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Subscription']")))
assert driver.find_element(By.XPATH, "//h2[text()='Subscription']").is_displayed()
driver.find_element(By.ID, "susbscribe_email").send_keys("test@example.com")
driver.find_element(By.ID, "subscribe").click()
wait.until(EC.visibility_of_element_located((By.ID, "success-subscribe")))
msg = driver.find_element(By.ID, "success-subscribe")
assert "You have been successfully subscribed!" in msg.text
print("TC10 Passed:", msg.text)
driver.quit()