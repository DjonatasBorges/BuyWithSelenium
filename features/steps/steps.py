from behave import given, when, then
from pages.login import Login
from time import sleep


@given(u'que eu esteja na página de login')
def page_login(context):
    context.driver.get('https://www.saucedemo.com/')
    sleep(3)


@when(u'preencher os dados de login')
def log_in(context):
    login = Login(context.driver)
    login.log_in()
    sleep(3)


@then(u'Então devo logar no site com sucesso.')
def confirmed_login(context):
    try:
        if context.driver.current_url == 'https://www.saucedemo.com/inventory.html':
            print('login efetuado com sucesso.')
    except:
        print('Deu ruim')
