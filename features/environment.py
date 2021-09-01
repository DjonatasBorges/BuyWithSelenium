from selenium import webdriver
from ipdb import post_mortem
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


def after_all(context):
    context.driver.quit()


