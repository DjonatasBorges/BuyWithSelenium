from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from login import Login
from products import Products
from checkout import CheckOut


class Setup:
    def before_all(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.link = 'https://www.saucedemo.com/'
        self.driver.get(self.link)
        self.driver.maximize_window()

    def execute_actions(self):
        self.login = Login(self.driver)
        self.produtos = Products(self.driver)
        self.checkout = CheckOut(self.driver)
        self.login.log_in()
        #filter
        self.produtos.filter()
        # selecionar produtos
        self.produtos.add_to_cart()
        # ir para o carrinho
        self.produtos.go_to_cart()
        # ir para o checkout
        self.produtos.go_to_checkout()
        # fechar pedido
        self.checkout.fill_in_checkout_data(self.driver, 'Djonatas', 'Borges', '13670-000')
        self.checkout.back_to_home(self.driver)


before = Setup()

before.before_all()
before.execute_actions()



