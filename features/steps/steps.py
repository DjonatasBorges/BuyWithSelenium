from behave import given, when, then
from selenium import webdriver
from pages.login import Login
from time import sleep


@given(u'que eu esteja na página de login')
def step(context):
    context.driver.get('https://www.saucedemo.com/')
    sleep(3)


@when(u'preencher os dados de login')
def step_login(context):
    login = Login(context.driver)
    login.log_in()
    sleep(3)


@then(u'Então devo logar no site com sucesso.')
def step_p(context):
    try:
        if context.driver.current_url == 'https://www.saucedemo.com/inventory.html':
            print('login efetuado com sucesso.')
    except:
        print('Deu ruim')
