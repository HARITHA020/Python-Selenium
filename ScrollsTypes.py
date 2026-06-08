from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
actions = ActionChains(driver)
# 1. scroll_by_amount()
print("Scrolling by amount")
actions.scroll_by_amount(0, 500).perform()
time.sleep(2)
# 2. scroll_to_element()
print("Scrolling to element")
table = driver.find_element(By.ID, "productTable")
actions.scroll_to_element(table).perform()
time.sleep(2)
# 3. scroll_from_origin()
print("Scrolling from origin")
origin = ScrollOrigin.from_element(table)
actions.scroll_from_origin(origin, 0, 300).perform()
time.sleep(2)
print("All scrolling actions completed.")
driver.quit()