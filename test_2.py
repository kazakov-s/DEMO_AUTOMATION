"""
    API-тесты. Работаем с SCAN Interfax.
"""

import pytest
import requests


class TestScanInterfax:
    BASE_URL = 'https://gateway.scan-interfax.ru'
    username = 'sf_student3'
    password = '6z9ZFRs'

    # Авторизуемся в API
    @pytest.mark.order(4)
    def test_authorisation(self):
        URL = self.BASE_URL + '/api/v1/account/login'
        headers = {'content-type': 'application/json'}
        req_data = {'login': self.username, 'password': self.password}
        response = requests.post(URL, headers=headers, json=req_data)
        assert response.status_code == 200
        res_data = response.json()
        assert 'accessToken' in res_data
        global auth_key
        auth_key = res_data['accessToken']

        print(auth_key)

    # Проверим баланс пользователя
    def test_user_balance(self):
        URL = self.BASE_URL + '/api/v1/account/balance'
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + auth_key}
        print(headers)
        response = requests.get(URL, headers=headers)
        assert response.status_code == 200
        res_data = response.json()
        assert 'balance' in res_data
        assert res_data['balance'] == 774193.00

        print(res_data)
