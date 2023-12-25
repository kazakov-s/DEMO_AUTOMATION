"""
    Модуль содержит тесты на авторизацию в сервисе Mail.Ru и автоматизированную
    отправку сообщения с вложением.
"""


from pages.login_form import LoginPage
from pages.compose_form import ComposeMessage


#Авторизацуемся на сервисе Mail.RU и проверяем, что авторизовались
def test_login(browser):
    auth_page = LoginPage(browser)
    auth_page.load()
    auth_page.login()
    auth_page.url_confirm()


#Формируем сообщение с вложением и проверяем корректность заполнения
def test_compose_message(browser):
    compose_page = ComposeMessage(browser)
    compose_page.compose()
    compose_page.compose_confirm()


# Отправляем сообщение и подтверждаем факт отправки
def test_send_message(browser):
    compose_page = ComposeMessage(browser)
    compose_page.send_message()
    compose_page.send_confirm()