import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
select_element = driver.find_element(By.ID, value="drop1")
select = Select(select_element)
dropdown_options = select.options
print(len(dropdown_options))
for option in dropdown_options:
  print(option.text)
select.select_by_visible_text("doc 2")
#select.select_by_index(4)  
#select.select_by_value("mno")
time.sleep(5)