from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Products:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.sauce_labs_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.sauce_labs_bike_light = (
            By.ID,
            "add-to-cart-sauce-labs-bike-light",
        )
        self.sauce_labs_bolt_t_shirt = (
            By.ID,
            "add-to-cart-sauce-labs-bolt-t-shirt",
        )
        self.sauce_labs_fleece_jacket = (
            By.ID,
            "add-to-cart-sauce-labs-fleece-jacket",
        )
        self.filterElements = (By.CLASS_NAME, "product_sort_container")
        self.source_labs_to_cartElement = (
            By.ID,
            "add-to-cart-sauce-labs-onesie",
        )
        self.test_all_theElement = (
            By.ID,
            "add-to-cart-test.allthethings()-t-shirt-(red)",
        )
        self.btn_cartElement = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.btn_checkout = (By.ID, "checkout")

    def filter_by(self, filter_text):
        dropdown = self.webdriver.find_element(*self.filterElements)
        dd = Select(dropdown)
        dd.select_by_visible_text(filter_text)

    def add_to_cart(self, product_list):
        produtos = product_list.split(",")
        for produto in produtos:
            pr1 = produto.lower().lstrip().replace(" ", "-")
            produto_cart = f"add-to-cart-{pr1}"
            self.webdriver.find_element_by_id(produto_cart).click()

    def go_to_cart(self):
        self.webdriver.find_element(*self.btn_cartElement).click()

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


class OnlyOneProduct:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.souce_labs_element = (
            By.XPATH,
            '//*[@id="item_2_title_link"]/div',
        )
        self.souce_labs_jacket = (By.XPATH, '//*[@id="item_5_title_link"]/div')
        self.btn_add_to_cart = (By.PARTIAL_LINK_TEXT, "Add to cart")
        self.btn_back_to_products = (By.ID, "back-to-products")
        self.total_value = (
            By.XPATH,
            '//*[@id="checkout_summary_container"]/div/div[2]/div[7]',
        )

    def add_product_to_cart(self, product_list):
        produtos = product_list.split(",")
        for produto in produtos:
            pr1 = produto.lower().lstrip().replace(" ", "-")
            produto_cart = f"add-to-cart-{pr1}"
            sleep(1)
            self.webdriver.find_element(
                By.PARTIAL_LINK_TEXT, produto.lstrip()
            ).click()
            sleep(1)
            self.webdriver.find_element(By.ID, produto_cart).click()
            sleep(1)
            self.webdriver.find_element(*self.btn_back_to_products).click()
            sleep(1)

    def confirmed_valor(self):
        return self.webdriver.find_element(*self.total_value).text
