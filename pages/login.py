from selenium.webdriver.common.by import By


class Login:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.usernameElement = (By.ID, "user-name")
        self.passwordElement = (By.ID, "password")
        self.btn_loginElement = (By.ID, "login-button")
        self.msg_error_login = (
            By.XPATH,
            '//*[@id="login_button_container"]/div/form/div[3]/h3',
        )

    def log_in(self, user, password):
        self.webdriver.find_element(*self.usernameElement).send_keys(user)
        self.webdriver.find_element(*self.passwordElement).send_keys(password)
        self.webdriver.find_element(*self.btn_loginElement).click()

    def error_login(self):
        msg = self.webdriver.find_element(*self.msg_error_login).text
        return msg
