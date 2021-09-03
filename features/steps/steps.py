from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.login import Login
from pages.products import Products
from pages.cart import Cart
from pages.checkout import CheckOut
from time import sleep

@given('que eu esteja na página de login')
def page_login(context):
    url = 'https://www.saucedemo.com/'
    context.driver.get(url)
    sleep(1)


@when(u'tentar efetuar login preenchendo os campos de usuario com "{user}" e de senha com "{password}"')
def step_impl(context, user, password):
    context.login = Login(context.driver)
    context.login.log_in(user, password)
    sleep(1)


@then(u'receber e validar mensagem de erro: "{msg}"')
def step_impl(context, msg):
    assert context.login.error_login() in msg
    sleep(1)


@given(u'que efetue login com campos de usuario com "{username}" e de senha com "{password}"')
def step_impl(context, username, password):
    url = 'https://www.saucedemo.com/'
    context.driver.get(url)
    sleep(1)
    context.login = Login(context.driver)
    context.login.log_in(username, password)
    sleep(1)


@given(u'que esteja na página de produtos.')
def step_impl(context):
    assert context.driver.current_url in 'https://www.saucedemo.com/inventory.html'
    sleep(1)


@when(u'filtrar "{filter}" e encontrar os produtos')
def step_impl(context, filter):
    context.products = Products(context.driver)
    context.products.filter_by(filter)
    sleep(1)


@when(u'clicar e inserir os produtos "{prod}" no carrinho de compras')
def step_impl(context, prod):
    context.conference_product = prod
    context.products.add_to_cart(prod)
    sleep(1)


@then(u'os produtos estão no carrinho')
def step_impl(context):
    context.products.go_to_cart()
    context.products.conference_go_checkout(context.conference_product)
    sleep(1)


@when(u'clicar no botão de checkout')
def step_impl(context):
    context.products.go_to_checkout()
    sleep(1)


@then(u'estar na página de checkout')
def step_impl(context):
    assert context.driver.current_url in 'https://www.saucedemo.com/checkout-step-one.html'
    sleep(1)


@when(u'preencher os dados do comprador com "{name}", "{lastname}" e dar continue.')
def step_error(context, name, lastname):
    context.checkout = CheckOut(context.driver)
    context.checkout.fill_in_checkout_error(name, lastname)
    sleep(1)


@then(u'mensagem de erro "{msg_error}"')
def step_impl(context, msg_error):
    if msg_error in context.driver.find_element_by_xpath("//h3[normalize-space()='Error: Postal Code is required']").text:
        btn_menu = 'react-burger-menu-btn'
        btn_logout = 'logout_sidebar_link'
        btn_reset = 'reset_sidebar_link'
        context.driver.find_element(By.ID, btn_menu).click()
        sleep(1)
        context.driver.find_element(By.ID, btn_reset).click()
        sleep(1)
        context.driver.find_element(By.ID, btn_logout).click()
        sleep(1)
    return False


@when(u'alocar dados do comprador com "{name}", "{lastname}" e "{postalcode}" e dar continue.')
def step_impl(context, name, lastname, postalcode):
    context.checkout = CheckOut(context.driver)
    context.checkout.fill_in_checkout_data(name, lastname, postalcode)
    sleep(1)


@then(u'estar na página de Overview e os produtos estão listados.')
def step_impl(context):
    assert context.driver.current_url in 'https://www.saucedemo.com/checkout-step-two.html'
    sleep(1)


@when(u'finalizar as compras')
def step_impl(context):
    context.checkout.finaly()
    sleep(1)


@then(u'compra finalizada com sucesso.')
def step_impl(context):
    assert context.driver.current_url in 'https://www.saucedemo.com/checkout-complete.html'
    sleep(1)
