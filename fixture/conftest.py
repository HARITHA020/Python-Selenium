import pytest
from selenium import webdriver

@pytest.fixture(params=['chrome','edge','firefox'])
def setup_and_teardown(request):
    if request.param=='chrome':
        driver=webdriver.Chrome()
    elif request.param=='edge':
        driver=webdriver.Edge()
    elif request.param=='firefox':
        driver=webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo")
    request.cls.driver = driver   
    yield
    driver.quit()