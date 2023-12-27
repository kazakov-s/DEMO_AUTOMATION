"""
    Модуль содержит фикстуры для UI - тестов
"""


import pytest
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='package')
# def browser():
#     driver = Chrome()
#     driver.implicitly_wait(10)
#
#     yield driver
#     driver.quit()

def browser():
    #    global driver
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()