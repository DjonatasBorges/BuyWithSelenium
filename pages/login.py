from selenium.webdriver.common.by import By


class Login:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.usernameElement = (By.ID, 'user-name')
        self.passwordElement = (By.ID, 'password')
        self.btn_loginElement = (By.ID, 'login-button')
        self.username = 'standard_user'
        self.password = 'secret_sauce'

    def log_in(self, user, password):
        self.webdriver.find_element(*self.usernameElement).send_keys(user)
        self.webdriver.find_element(*self.passwordElement).send_keys(password)
        self.webdriver.find_element(*self.btn_loginElement).click()

