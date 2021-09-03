from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()


def after_all(context):
    context.driver.quit()
    sleep(3)


'''def after_scenario(context):
    btn_menu = 'react-burger-menu-btn'
    btn_logout = 'logout_sidebar_link'
    btn_reset = 'reset_sidebar_link'
    context.driver.find_element(By.ID, btn_menu).click()
    sleep(1)
    context.driver.find_element(By.ID, btn_reset).click()
    sleep(1)
    context.driver.find_element(By.ID, btn_logout).click()
    sleep(4)'''




