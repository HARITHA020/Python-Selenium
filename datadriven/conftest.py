import pytest
from selenium import webdriver
import readconfig
@pytest.fixture()
def setup_and_teardown(request):
    browser = readconfig.get_config("basic info", "browser")
    url = readconfig.get_config("basic info", "url")
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Browser not supported")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()