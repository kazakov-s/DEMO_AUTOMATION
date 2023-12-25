"""
    Модуль содержит фикстуры для UI - тестов
"""


import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope='package')
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()

