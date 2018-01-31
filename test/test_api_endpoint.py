from flask import json
from test import BaseAppApiTest

INVALID_SIGN_UP_DATA = {
    'username': 'test123',
    'email': 'test@example.com',
    'password': '22332'
}

VALID_SIGN_UP_DATA = {
    'username': 'test123',
    'email': 'test@example.com',
    'password': 'Debb23'
}

VALID_LOGIN_DATA = {
    'email': 'test@example.com',
    'password': 'Debb23'
}

INVALID_LOGIN_DATA = {
    'email': 'te@example.com',
    'password': 'Debb23'
}

class TestApiEndpoint(BaseAppApiTest):

    base_api_url = 'api/v1/'

    def registration(self, request_data):
        url = TestApiEndpoint.base_api_url + 'signup'
        response = self.app_client.post(url, data=json.dumps(request_data),
                headers={
                    'content-type': 'application/json'
                })
        data = json.loads(response.get_data())
        return data

    def logout(self, token):
        url = TestApiEndpoint.base_api_url + 'logout'
        response = self.app_client.post(url, 
                headers={
                    'content-type': 'application/json',
                    'Authorization': 'Bearer %s' % token 
                })
        data = json.loads(response.get_data())
        return data
    
    def login(self, request_data):
        url = TestApiEndpoint.base_api_url + 'login'
        response = self.app_client.post(url, data=json.dumps(request_data),
                headers={
                    'content-type': 'application/json'
                })
        data = json.loads(response.get_data())
        return data

    def test_registration_endpoint_with_invalid_data(self):
        data = self.registration(INVALID_SIGN_UP_DATA)
        self.assertEqual('error', data['status'])
        self.assertEqual('VALIDATION_ERROR', data['error_type'])
    
    def test_reistration_endpoint_with_valid_data(self):
        data = self.registration(VALID_SIGN_UP_DATA)
        self.assertEqual('success', data['status'])
        self.assertIn('login_token', data.keys())

    def test_endpoint_without_authorization(self):
        url = TestApiEndpoint.base_api_url + 'test'
        response = self.app_client.get(url, headers={
            'content-type': 'application/json'
        })
        data = json.loads(response.get_data())
        print(data)
        self.assertEqual('AUTHORIZATION_HEADER_ERROR', data['error_type'])

    def test_endpoint_with_authorization_but_not_type_bearer(self):
        url = TestApiEndpoint.base_api_url + 'test'
        response = self.app_client.get(url, headers={
            'content-type': 'application/json',
            'Authorization': 'bgjkbjsblknesklkenrknfnekwnlfklwneflkdnsknewkdsflkendlfnkle'
        })
        data = json.loads(response.get_data())
        print(data)
        self.assertEqual('AUTHORIZATION_HEADER_ERROR', data['error_type'])
        self.assertEqual(data['message'], 'Authorization type must be Bearer Token')

    def test_login_endpoint_with_valid_data(self):
        new_user = self.registration(VALID_SIGN_UP_DATA)
        token = new_user['login_token']
        self.logout(token)
        data = self.login(VALID_LOGIN_DATA)
        print(data)
        self.assertEqual('success', data['status'])
        self.assertEqual(data['message'], 'login successfull')
        self.assertIn('login_token', data.keys())
    
    def test_login_endpoint_with_invalid_data(self):
        new_user = self.registration(VALID_SIGN_UP_DATA)
        token = new_user['login_token']
        self.logout(token)
        data = self.login(INVALID_LOGIN_DATA)
        print(data)
        self.assertEqual('error', data['status'])
        self.assertEqual(data['error_type'], 'AUTHENTICATION_ERROR')
