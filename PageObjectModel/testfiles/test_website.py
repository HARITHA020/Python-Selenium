import pytest
import readconfig

from pages.LoginPage import LoginPage
from pages.Homepage import HomePage
from pages.searchPage import SearchPage
from pages.product import ProductPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestWebsite:

    @pytest.mark.dependency(name="login")
    def test_login(self):
        login = LoginPage(self.driver)
        username = readconfig.get_config("login credential","uname")
        password = readconfig.get_config("login credential","upass")
        login.enter_form_details(username, password)
        assert "My Account" in self.driver.page_source

    @pytest.mark.dependency(depends=["login"],name="home")
    def test_home(self):

        homepage = HomePage(self.driver)
        product = readconfig.get_config("search term","validterm")
        homepage.enter_product(product)
        homepage.click_search()

    @pytest.mark.dependency(depends=["home"],name="search")
    def test_search(self):
        searchpage = SearchPage(self.driver)
        assert searchpage.verify_product()
    @pytest.mark.dependency(depends=["search"])
    def test_product(self):
        productpage = ProductPage(self.driver)
        productpage.click_product_link()
        productpage.click_add_to_cart()
        msg = productpage.get_success_message()
        assert "Success: You have added HP LP3065 to your shopping cart!" in msg
        print(msg)