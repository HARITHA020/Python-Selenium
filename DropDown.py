from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver= webdriver.Chrome()
driver.get("https://leafground.com/select.xhtml")
dropicon=Select(driver.find_element(By.XPATH,"//select[@class='ui-selectonemenu']"))
#dropicon.select_by_index(4)
dropicon.select_by_visible_text("Cypress")
driver.close()
