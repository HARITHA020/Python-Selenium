import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("input", ['chrome', 'edge'])
@pytest.mark.parametrize("url", ['https://www.flipkart.com', 'https://www.amazon.com'])
def test_url_on_browsers(input, url):
    if input == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Chrome(options=options)
    elif input == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--headless") 
        web_driver = webdriver.Edge(options=options)
    web_driver.maximize_window()
    web_driver.get(url)
    print(web_driver.title)
    time.sleep(2)
    web_driver.quit()
    