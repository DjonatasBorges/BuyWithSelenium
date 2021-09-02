from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Products:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.sauce_labs_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.sauce_labs_bike_light = (By.ID, 'add-to-cart-sauce-labs-bike-light')
        self.sauce_labs_bolt_t_shirt = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
        self.sauce_labs_fleece_jacket = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        self.filterElements = (By.CLASS_NAME, 'product_sort_container')
        self.source_labs_to_cartElement = (By.ID, 'add-to-cart-sauce-labs-onesie')
        self.test_all_theElement = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
        self.btn_cartElement = (By.CSS_SELECTOR, '.shopping_cart_link')
        self.btn_checkout = (By.ID, 'checkout')

    def filter(self, filter_text):
        dropdown = self.webdriver.find_element(*self.filterElements)
        dd = Select(dropdown)
        dd.select_by_visible_text(filter_text)

    def add_to_cart(self, product_list):
        produtos = product_list.split(',')
        for produto in produtos:
            pr1 = produto.lower().lstrip().replace(' ', '-')
            produto_cart = f'add-to-cart-{pr1}'
            self.webdriver.find_element_by_id(produto_cart).click()

    def go_to_cart(self):
        self.webdriver.find_element(*self.btn_cartElement).click()

    def go_to_checkout(self):
        self.webdriver.find_element(*self.btn_checkout).click()
