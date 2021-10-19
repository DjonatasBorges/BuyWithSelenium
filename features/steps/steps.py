from time import sleep

from behave import given
from behave import then
from behave import when
from selenium.webdriver.common.by import By

from pages.checkout import CheckOut
from pages.login import Login
from pages.products import OnlyOneProduct
from pages.products import Products


@given("que eu esteja na página de login")
def page_login(context):
    url = "https://www.saucedemo.com/"
    context.driver.get(url)
    sleep(1)


@when('tentar efetuar login preenchendo os campos de usuario com "{user}" e de senha com "{password}"')
def fail_login(context, user, password):
    context.login = Login(context.driver)
    context.login.log_in(user, password)
    sleep(1)


@then('receber e validar mensagem de erro: "{msg}"')
def error_msg(context, msg):
    assert context.login.error_login() in msg
    sleep(1)


@given('que efetue login com campos de usuario com "{username}" e de senha com "{password}"')
def login(context, username, password):
    url = "https://www.saucedemo.com/"
    context.driver.get(url)
    sleep(1)
    context.login = Login(context.driver)
    context.login.log_in(username, password)
    sleep(1)


@given("que esteja na página de produtos.")
def product_page(context):
    assert context.driver.current_url in "https://www.saucedemo.com/inventory.html"
    sleep(1)


@when('filtrar "{filter}" e encontrar os produtos')
def filter_producuts(context, filter):
    context.products = Products(context.driver)
    context.products.filter_by(filter)
    sleep(1)


@when('clicar e inserir os produtos "{prod}" no carrinho de compras')
def insert_cart(context, prod):
    context.prod = prod
    context.products.add_to_cart(context.prod)
    sleep(1)


@then("os produtos estão no carrinho")
def products_in_the_cart(context):
    context.products.go_to_cart()
    context.products.conference_go_checkout(context.prod)
    sleep(1)


@when("clicar no botão de checkout")
def btn_checkout(context):
    context.products.go_to_checkout()
    sleep(1)


@then("estar na página de checkout")
def checkout_page(context):
    assert context.driver.current_url in "https://www.saucedemo.com/checkout-step-one.html"
    sleep(1)


@when('preencher os dados do comprador com "{name}", "{lastname}" e dar continue.')
def data_(context, name, lastname):
    context.checkout = CheckOut(context.driver)
    context.checkout.fill_in_checkout_error(name, lastname)
    sleep(1)


@then('mensagem de erro "{msg_error}"')
def mmsg_error_postal_code(context, msg_error):
    if (
        msg_error
        in context.driver.find_element_by_xpath("//h3[normalize-space()='Error: Postal Code is required']").text
    ):
        btn_menu = "react-burger-menu-btn"
        btn_logout = "logout_sidebar_link"
        btn_reset = "reset_sidebar_link"
        context.driver.find_element(By.ID, btn_menu).click()
        sleep(1)
        context.driver.find_element(By.ID, btn_reset).click()
        sleep(1)
        context.driver.find_element(By.ID, btn_logout).click()
        sleep(1)
    return False


@when('alocar dados do comprador com "{name}", "{lastname}" e "{postalcode}" e dar continue.')
def realocation_data(context, name, lastname, postalcode):
    context.checkout = CheckOut(context.driver)
    context.checkout.fill_in_checkout_data(name, lastname, postalcode)
    sleep(1)


@then("estar na página de Overview e os produtos estão listados.")
def overview_page(context):
    assert context.driver.current_url in "https://www.saucedemo.com/checkout-step-two.html"
    sleep(1)


@when("finalizar as compras")
def finish_purchase(context):
    context.checkout.finaly()
    sleep(1)


@then("compra finalizada com sucesso.")
def susseful_purchase(context):
    assert context.driver.current_url in "https://www.saucedemo.com/checkout-complete.html"
    sleep(1)


@when('clicar, ir e inserir os produtos "{produtos}" no carrinho de compras')
def cart_step(context, produtos):
    context.only_product = OnlyOneProduct(context.driver)
    context.only_product.add_product_to_cart(produtos)
    context.products = Products(context.driver)
    context.products.go_to_cart()
    context.prod = produtos


@then('valor da compra ser igual a "{valor}"')
def value(context, valor):
    assert valor in context.only_product.confirmed_valor()
