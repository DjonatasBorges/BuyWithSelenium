from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class Products:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.filterElements = (By.CLASS_NAME, 'product_sort_container')
        self.source_labs_to_cartElement = (By.ID, 'add-to-cart-sauce-labs-onesie')
        self.test_all_theElement = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
        self.btn_cartElement = (By.CSS_SELECTOR, '.shopping_cart_link')
        self.btn_checkout = (By.ID, 'checkout')

    def filter(self):
        dropdown = self.webdriver.find_element(*self.filterElements)
        dd = Select(dropdown)
        dd.select_by_value('lohi')

    def add_to_cart(self):
        self.webdriver.find_element(*self.source_labs_to_cartElement).click()
        self.webdriver.find_element(*self.test_all_theElement).click()
        sleep(2)

    def go_to_cart(self):
        self.webdriver.find_element(*self.btn_cartElement).click()
        
    def go_to_checkout(self):
        self.webdriver.find_element(*self.btn_checkout).click()
