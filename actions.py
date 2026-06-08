from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver= webdriver.Chrome()
wait= WebDriverWait(driver,30)
driver.maximize_window()
driver.get("https://leafground.com/drag.xhtml")
drag=driver.find_element(By.XPATH,"//*[@id='form:drag_content']")
drop=driver.find_element(By.XPATH,"//*[@id='form:drop_content']")
action=ActionChains(driver)
action.click_and_hold(drag).move_to_element(drop).release().perform()
print("drag is happen successfully")
driver.close()