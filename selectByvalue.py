from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("https://leafground.com/select.xhtml")
dropdown = Select(driver.find_element(By.ID, "j_idt87:country_input"))
for option in dropdown.options:
    print(option.text, option.get_attribute("value"))


