"""
    UI-тесты. Автоматизация отправки сообщения с вложением через сервис Mail.Ru с последующими проверками заполнения полей и отправки.
"""

from pages.login_form import LoginPage
from pages.compose_form import ComposeMessage
import allure
import pytest


# Авторизацуемся на сервисе Mail.RU и проверяем, что авторизовались
@pytest.mark.order(1)
@allure.suite("Авторизация")
@allure.title('Заполняем форму авторизации и проверяем успешность авторизации')
@allure.description(
    f'Авторизация в почтовом сервисе Mail.Ru с валидными данными.')
@allure.tag('AUTHENTICATION')
@allure.severity(allure.severity_level.BLOCKER)
@allure.label('Developer', 'Sergey Kazakov')
def test_login(browser):
    auth_page = LoginPage(browser)
    auth_page.load()
    auth_page.login()
    auth_page.url_confirm()


# Формируем сообщение с вложением и проверяем корректность заполнения
@pytest.mark.order(2)
@allure.suite("Формирование сообщения")
@allure.title('Проверяем поля сообщения на корректность заполнения')
@allure.description('Проверяем поля сообщения на соответствие данным, полученным из файла data.ini')
@allure.tag('INPUTS EXPECTATION')
@allure.severity(allure.severity_level.BLOCKER)
@allure.label('Developer', 'Sergey Kazakov')
def test_compose_message(browser):
    compose_page = ComposeMessage(browser)
    compose_page.compose()
    compose_page.compose_confirm()


# Отправляем сообщение и подтверждаем факт отправки
@pytest.mark.order(3)
@allure.suite("Формирование сообщения")
@allure.title('Отправка сообщения')
@allure.description('Отправка сообщения')
@allure.tag('SEND MESSAGE')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('Developer', 'Sergey Kazakov')
def test_send_message(browser):
    compose_page = ComposeMessage(browser)
    compose_page.send_message()
    compose_page.send_confirm()