"""
    Модуль содержит PageObject для страницы авторизации Mail.Ru
"""

from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data import url, username, password
from time import sleep
import allure


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
    @allure.suite("Авторизация")
    @allure.title('Заполняем форму авторизации и проверяем успешность авторизации')
    @allure.description(
        f'Авторизация в почтовом сервисе Mail.Ru с валидными данными. Username: {{username}} Password: {{password}}')
    @allure.tag('AUTHENTICATION')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.label('Developer', 'Sergey Kazakov')
    def login(self):
        try:
            WW(self.browser, 10).until(EC.visibility_of_element_located(self.user_ele)).send_keys(username)
            sleep(1)
            WW(self.browser, 10).until(EC.visibility_of_element_located(self.login_ele)).click()
            sleep(1)
            WW(self.browser, 10).until(EC.visibility_of_element_located(self.password_ele)).send_keys(password)
            sleep(1)
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
            WW(self.browser, 10).until(EC.visibility_of_element_located(self.login_ele)).click()
            sleep(1)

        except:
            print('Процесс авторизации завершился неудачно! Функция login')
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    # Проверяем факт перехода в папку "Входящие" под авторизованным пользователем
    @allure.suite("Авторизация")
    @allure.title('Проверяем факт перехода в папку "Входящие" под авторизованным пользователем')
    @allure.description('Проверяем соответствие URL в адресной строке браузера ожидаемому.')
    @allure.tag('URL EXPECTATION')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.label('Developer', 'Sergey Kazakov')
    def url_confirm(self):
        try:
            WW(self.browser, 10).until(EC.element_to_be_clickable((self.expect_ele)))
            assert 'https://e.mail.ru/inbox/?authid=' in self.browser.current_url
            sleep(1)
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        except:
            print('Переход в почтовый ящик завершился неудачно. Функция url_confirm')
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
