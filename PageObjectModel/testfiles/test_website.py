import pytest
import readconfig

from pages.LoginPage import LoginPage
from pages.Homepage import HomePage
from pages.searchPage import SearchPage
from pages.product import ProductPage
from utilities import logCreator

@pytest.mark.usefixtures("setup_and_teardown")
class TestWebsite:
    log = logCreator.log_generator()
    @pytest.mark.dependency(name="login")
    def test_login(self):
        self.log.info("*** Login Test Started ****")
        login = LoginPage(self.driver)
        username = readconfig.get_config("login credential", "uname")
        password = readconfig.get_config("login credential", "upass")
        self.log.info(f"Entering Username : {username}")
        login.enter_form_details(username, password)
        self.log.info("Clicked Login Button")
        assert "My Account" in self.driver.page_source
        self.log.info("Login Successful")
        self.log.info("**** Login Test Passed *****")

    @pytest.mark.dependency(depends=["login"], name="home")
    def test_home(self):

        self.log.info("*** Home Test Started ****")
        homepage = HomePage(self.driver)
        product = readconfig.get_config("search term", "validterm")
        self.log.info(f"Searching Product : {product}")
        homepage.enter_product(product)
        homepage.click_search()
        self.log.info("Search Button Clicked")
        self.log.info("*** Home Test Passed *****")

    @pytest.mark.dependency(depends=["home"], name="search")
    def test_search(self):

        self.log.info("** Search Test Started ***")

        searchpage = SearchPage(self.driver)

        assert searchpage.verify_product()

        self.log.info("Product Displayed Successfully")
        self.log.info("** Search Test Passed ****")

    @pytest.mark.dependency(depends=["search"])
    def test_product(self):

        self.log.info("*** Product Test Started ***")

        productpage = ProductPage(self.driver)

        self.log.info("Opening Product Page")
        productpage.click_product_link()

        self.log.info("Clicking Add To Cart")
        productpage.click_add_to_cart()

        msg = productpage.get_success_message()

        self.log.info(f"Success Message : {msg}")

        assert "Success: You have added HP LP3065 to your shopping cart!" in msg

        self.log.info("Product Added To Cart Successfully")
        self.log.info("*** Product Test Passed ****")