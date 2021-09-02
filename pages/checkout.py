from selenium.webdriver.common.by import By
from time import sleep


class CheckOut:
    def __init__(self, webdriver):
        self.first_nameElement = (By.ID, 'first-name')
        self.last_nameElement = (By.ID, 'last-name')
        self.postal_codeElement = (By.ID, 'postal-code')
        self.submit = (By.ID, 'continue')
        self.final = (By.ID, 'finish')
        self.webdriver = webdriver
        self.btn_back_home = (By.ID, 'back-to-products')

    def fill_in_checkout_data(self, first_name, last_name, postal_code):
        self.webdriver.find_element(*self.first_nameElement).send_keys(first_name)
        self.webdriver.find_element(*self.last_nameElement).send_keys(last_name)
        self.webdriver.find_element(*self.postal_codeElement).send_keys(postal_code)
        self.webdriver.find_element(*self.submit).click()

    def back_to_home(self):
        self.webdriver.find_element(*self.final).click()
        self.webdriver.find_element(*self.btn_back_home).click()
        sleep(3)
        self.webdriver.quit()
