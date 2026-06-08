import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
select_element = driver.find_element(By.ID, value="multiselect1")
select = Select(select_element)
multiselect_options = select.options
print(len(multiselect_options))
for option in multiselect_options:
  print(option.text)
select.select_by_visible_text("Swift")
select.select_by_index(0)
select.select_by_value("audix")
time.sleep(5)
select.deselect_by_visible_text("Swift")
select.deselect_by_index(0)
select.deselect_by_value("audix")
#select.deselect_all()
time.sleep(5)
select.select_by_visible_text("Hyundai")