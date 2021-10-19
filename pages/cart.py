from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Cart:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.btn_checkout = (By.ID, "checkout")
        self.cart_url = "https://www.saucedemo.com/cart.html"
        self.btn_continue = (By.ID, "continue-shopping")

    def conference_go_checkout(self, product_list):
        produtos = product_list.split(",")
        for produto in produtos:
            if (
                produto
                in self.webdriver.find_element(
                    By.PARTIAL_LINK_TEXT, produto
                ).text
            ):
                return True
            return False

    def go_to_checkout(self):
        self.webdriver.find_element(*self.btn_checkout).click()
