from seleniumpagefactory.Pagefactory import PageFactory

class SearchPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'valid_product': ('LINK_TEXT', "HP LP3065")
    }

    def get_display_status_of_valid_product(self):
        return self.valid_product.is_displayed()