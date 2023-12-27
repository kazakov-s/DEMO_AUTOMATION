"""
    API-тесты. Работаем с SCAN Interfax.
"""

import pytest
import requests


class TestScanInterfax:
    BASE_URL = 'https://gateway.scan-interfax.ru'
    username = 'sf_student3'
    password = '6z9ZFRs'
    id1 = '1:0JPQqdGM0JNWCdCzf2Jt0LHQotGV0ZUh0ZbRlBXCt0Je0JHQruKAnDcUXkZQ0YvQscKnehLRnNC1KtGK0Ll9BWLigLo/HXXCrhw='
    id2 = '1:fmYoHEjQrRbQhz3RiUtm4oCh0JLRmtCLIyU10IzigqzRgGjQmCoR0JFg0YRhwrVzN9CxDUM50KcpdTbRiNCLwpjRkuKAphXRkVxh0JU50K5uWdC50L7RjX0C0KwQRsKp'


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
        auth_key = res_data['accessToken']
        return auth_key


    # Проверим баланс пользователя
    @pytest.mark.order(5)
    def test_user_balance(self):
        auth_key = self.test_authorisation()
        URL = self.BASE_URL + '/api/v1/account/balance'
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + auth_key}
        response = requests.get(URL, headers=headers)
        assert response.status_code == 200
        res_data = response.json()
        assert 'balance' in res_data
        assert res_data['balance'] == 774193.00

    # Получим темы публикаций
    @pytest.mark.order(6)
    def test_publication_topics(self):
        auth_key = self.test_authorisation()
        URL = self.BASE_URL + '/api/v1/entities/subjects'
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + auth_key}
        params = {'index': 0, 'pageSize': 10}
        response = requests.get(URL, headers=headers, params=params)
        assert response.status_code == 200
        assert response.json()['subjects'][0]['name'] == 'Административная и хозяйственная деятельность'

    # Получим документы
    @pytest.mark.order(7)
    def test_documents(self):
        auth_key = self.test_authorisation()
        URL = self.BASE_URL + '/api/v1/documents'
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + auth_key}
        req_data = {
            'ids': [
                self.id1,
                self.id2
            ]
        }
        response = requests.post(URL, headers=headers, json=req_data)
        res_data = response.json()
        assert response.status_code == 200
        assert res_data[0]['ok']['id'] == self.id1
        assert res_data[1]['ok']['id'] == self.id2
        assert res_data[0]['ok']['source']['name'] == 'Вести.Ru (vesti.ru)'
        assert res_data[1]['ok']['source']['name'] == 'Аргументы и Факты - Казань (kazan.aif.ru)'
