from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

driver.maximize_window()
driver.get("https://leafground.com/window.xhtml")

parent_window = driver.current_window_handle

driver.find_element(By.XPATH, "//*[@id='j_idt88:new']").click()

all_windows = driver.window_handles

for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break
print("Child Window Title:", driver.title)

driver.switch_to.window(parent_window)

print("Parent Window Title:", driver.title)

driver.quit()