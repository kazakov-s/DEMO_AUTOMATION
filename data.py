"""
    Модуль содержит функции загрузки тестовых данных и создания файла вложения
"""

import os
import configparser

# Читаем конфиг
config = configparser.ConfigParser()

# config['DEFAULT'] = {'url': 'https://e.mail.ru/inbox/',
#                     'username': 'mikhail.zavyalov.00@internet.ru',
#                     'pass': 'Wcppos321',
#                     'email': 'kazackov.s@yandex.ru',
#                     'title': 'This is a great subject for my letter',
#                     'text': 'This is a great text for my letter',
#                     'path': 'attachment.txt'}
#
# with open('data.ini', 'w', encoding='utf-8') as configfile: config.write(configfile)


config.read('data.ini')

url = config.get('DEFAULT', 'url')
username = config.get('DEFAULT', 'username')
password = config.get('DEFAULT', 'pass')
email = config.get('DEFAULT', 'email')
title = config.get('DEFAULT', 'title')
text = config.get('DEFAULT', 'text')
full_path = os.path.dirname(os.path.abspath(__file__)) + '\\' + config.get('DEFAULT', 'path')
path = config.get('DEFAULT', 'path')


# Создаем файл вложения
with open('attachment.txt', 'w', encoding='utf-8') as f:
    string = 'Привет!'
    f.write(string)
    f.close()
