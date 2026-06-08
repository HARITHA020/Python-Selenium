from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
def type_date(element, date):
    driver.execute_script("arguments[0].value='"+date+"'", element)
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
calendar = driver.find_element(By.ID, value="datepicker")
type_date(calendar, '09/02/2024')
driver.quit()