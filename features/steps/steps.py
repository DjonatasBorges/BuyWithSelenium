from behave import given, when, then
from pages.login import Login
from pages.products import Products
from pages.checkout import CheckOut
from time import sleep


@given('que eu esteja na página de login')
def page_login(context):
    url = 'https://www.saucedemo.com/'
    context.driver.get(url)
    sleep(1)


@when('efetuar login preenchendo os campos de usuario com "{standard_user}" e de senha com "{secret_sauce}"')
def log_in(context, standard_user, secret_sauce):
    login = Login(context.driver)
    login.log_in(standard_user, secret_sauce)
    sleep(1)


@then('devo logar no site com sucesso.')
def confirmed_login(context):
    assert context.driver.current_url in 'https://www.saucedemo.com/inventory.html'
    sleep(1)


@given('que esteja na página de produtos')
def page_products(context):
    assert context.driver.current_url in 'https://www.saucedemo.com/inventory.html'


@when('filtrar "{filtro}" e encontrar os produtos')
def find_products(context, filtro):
    context.products = Products(context.driver)
    context.products.filter(filtro)


@then('clicar e inserir os produtos "{produtos}" no carrinho de compras')
def add_to_cart(context, produtos):
    context.products.add_to_cart(produtos)
    sleep(3)


@then('clicar para ir para o carrinho.')
def go_tocart(context):
    context.products.go_to_cart()
    sleep(3)


@given(u'que esteja na página do carrinho.')
def page_car(context):
    assert context.driver.current_url in 'https://www.saucedemo.com/cart.html'


@when('conferir se os produtos "{produtos}" estão no carrinho e ir para o checkout')
def conference_go_checkout(context, produtos):
    context.products = Products(context.driver)
    context.products.conference_go_checkout(produtos)
    context.products.go_to_checkout()
    sleep(2)


@when('preencher os dados do comprador com "{first_name}", "{last_name}" e "{postal_code}"')
def check_out(context, first_name, last_name, postal_code):
    context.checkout = CheckOut(context.driver)
    context.checkout.fill_in_checkout_data(first_name, last_name, postal_code)
    sleep(2)


@then('finalizar a compra e voltar para o home.')
def final(context):
    context.checkout.back_to_home()

