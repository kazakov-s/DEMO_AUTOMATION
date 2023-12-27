"""
    Модуль содержит PageObject для страницы формирования сообщения
"""

from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from data import email, title, text, full_path, path
from time import sleep
import allure


class ComposeMessage:
    compose_ele = (By.XPATH, '//a[@title="Написать письмо"]')
    address_ele = (By.XPATH, '//input[@class="container--H9L5q size_s--3_M-_"]')
    subject_ele = (By.XPATH, '//input[@name="Subject"]')
    text_ele = (By.XPATH, '//div[@role="textbox"]/div')
    attach_ele = (By.XPATH, '// input[@type="file"]')
    send_ele = (By.XPATH, '//button[@data-test-id="send"]')
    confirm_ele = (By.XPATH, '//a[text()="Письмо отправлено"]')

    confirm_address = (By.XPATH, '//span[text()="kazackov.s@yandex.ru"]')
    confirm_attachment = (By.XPATH, '//span[text()="attachment.txt"]')

    def __init__(self, browser):
        self.browser = browser

    # Заполняем поля сообщения тестовыми данными из файла
    @allure.suite("Формирование сообщения")
    @allure.title('Заполняем поля сообщения тестовыми данными из файла')
    @allure.description(f'Заполняем поля сообщения тестовыми данными из файла')
    @allure.tag('COMPOSE MESSAGE')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label('Developer', 'Sergey Kazakov')
    def compose(self):
        try:
            with allure.step("Step 1"):
                WW(self.browser, 10).until(EC.presence_of_element_located(self.compose_ele)).click()
                sleep(1)
                allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot',
                              attachment_type=AttachmentType.PNG)
            with allure.step("Step 2"):
                WW(self.browser, 10).until(EC.visibility_of_element_located(self.address_ele)).send_keys(email)
                sleep(1)
                allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot',
                              attachment_type=AttachmentType.PNG)
            with allure.step("Step 3"):
                WW(self.browser, 10).until(EC.visibility_of_element_located(self.subject_ele)).send_keys(title)
                sleep(1)
                allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot',
                              attachment_type=AttachmentType.PNG)
            with allure.step("Step 4"):
                WW(self.browser, 10).until(EC.visibility_of_element_located(self.text_ele)).send_keys(text)
                sleep(1)
                allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot',
                              attachment_type=AttachmentType.PNG)
            with allure.step("Step 5"):
                WW(self.browser, 10).until(EC.presence_of_element_located(self.attach_ele)).send_keys(full_path)
                sleep(1)
                allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot',
                              attachment_type=AttachmentType.PNG)
        except:
            print('Заполнение полей сообщения завешилось неудачно! Функция compose')
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    # Проверяем поля сообщения на корректность заполнения
    def compose_confirm(self):
        address = WW(self.browser, 10).until(EC.presence_of_element_located(self.confirm_address)).text
        assert address == email
        subject = WW(self.browser, 10).until(EC.presence_of_element_located(self.subject_ele))
        subject = subject.get_attribute('value')
        assert subject == title
        message = WW(self.browser, 10).until(EC.presence_of_element_located(self.text_ele)).text
        assert message == text
        attachment = WW(self.browser, 10).until(EC.presence_of_element_located(self.confirm_attachment)).text
        assert attachment == path
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    # Отправляем сообщение
    def send_message(self):
        try:
            WW(self.browser, 10).until(EC.presence_of_element_located(self.send_ele)).click()
            sleep(1)
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        except:
            print('Отправка сообщения завершилась неудачно! Функция send_message')
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    # Проверяем факт отправки сообщения
    def send_confirm(self):
        assert WW(self.browser, 10).until(EC.element_to_be_clickable(self.confirm_ele))
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
