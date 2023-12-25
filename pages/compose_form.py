"""
    Модуль содержит PageObject для страницы формирования сообщения
"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from data import email, title, text, path
from time import sleep


class ComposeMessage:
    compose_ele = (By.XPATH, '//a[@title="Написать письмо"]')
    address_ele = (By.XPATH, '//input[@class="container--H9L5q size_s--3_M-_"]')
    subject_ele = (By.XPATH, '//input[@name="Subject"]')
    text_ele = (By.XPATH, '//div[@role="textbox"]/div')
    attach_ele = (By.XPATH, '// input[@type="file"]')
    send_ele = (By.XPATH, '//button[@data-test-id="send"]')
    confirm_ele = (By.XPATH, '//a[text()="Письмо отправлено"]')

    def __init__(self, browser):
        self.browser = browser


    def compose(self):
        try:
            WW(self.browser, 10).until(EC.presence_of_element_located(self.compose_ele)).click()
            sleep(1)
            WW(self.browser, 10).until(EC.visibility_of_element_located(self.address_ele)).send_keys(email)
            sleep(1)
            WW(self.browser, 10).until(EC.visibility_of_element_located(self.subject_ele)).send_keys(title)
            sleep(1)
            WW(self.browser, 10).until(EC.visibility_of_element_located(self.text_ele)).send_keys(text)
            sleep(1)
            WW(self.browser, 10).until(EC.presence_of_element_located(self.attach_ele)).send_keys(path)
            sleep(1)

        except:
            print('Заполнение полей сообщения завешилось неудачно! Функция compose')



    def send_confirm(self):
        try:
            WW(self.browser, 10).until(EC.presence_of_element_located(self.send_ele)).click()
            sleep(1)
            assert WW(self.browser, 10).until(EC.element_to_be_clickable(self.confirm_ele))
            sleep(3)

        except:
            print('Отправка сообщения завершилась неудачно! Функция send_confirm')


