"""
    Модуль содержит PageObject для страницы авторизации Mail.Ru
"""

from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data import url, username, password
from time import sleep


class LoginPage:
    user_ele = (By.XPATH, '//input[@name="username"]')
    password_ele = (By.XPATH, '//input[@name="password"]')
    login_ele = (By.XPATH, '//button[@type="submit"]')
    expect_ele = (By.XPATH, '//a[@title="Написать письмо"]')

    def __init__(self, browser):
        self.browser = browser


    def load(self):
        self.browser.get(url)

    #Заполняем форму авторизации и проверяем успешность авторизации
    def login(self):
        try:
            WW(self.browser, 10).until(EC.visibility_of_element_located(self.user_ele)).send_keys(username)
            sleep(1)
            WW(self.browser, 10).until(EC.visibility_of_element_located(self.login_ele)).click()
            sleep(1)
            WW(self.browser, 10).until(EC.visibility_of_element_located(self.password_ele)).send_keys(password)
            sleep(1)
            WW(self.browser, 10).until(EC.visibility_of_element_located(self.login_ele)).click()
            sleep(1)

        except:
            print('Процесс авторизации завершился неудачно! Функция login')


    def url_confirm(self):
        try:
            WW(self.browser, 10).until(EC.element_to_be_clickable((self.expect_ele)))
            assert 'https://e.mail.ru/inbox/?authid=' in self.browser.current_url
            sleep(1)
        except:
            print('Переход в почтовый ящик завершился неудачно. Функция url_confirm')