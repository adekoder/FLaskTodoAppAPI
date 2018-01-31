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

class TestApiEndpoint(BaseAppApiTest):

    base_api_url = 'api/v1/'

    def test_registration_endpoint_with_invalid_data(self):
        url = TestApiEndpoint.base_api_url + 'signup'
        response = self.app_client.post(url, data=json.dumps(INVALID_SIGN_UP_DATA),
                headers={
                    'content-type': 'application/json'
                })
        data = json.loads(response.get_data())
        self.assertEqual('error', data['status'])
        self.assertEqual('VALIDATION_ERROR', data['error_type'])
    
    def test_reistration_endpoint_with_valid_data(self):
        url = TestApiEndpoint.base_api_url + 'signup'
        response = self.app_client.post(url, data=json.dumps(VALID_SIGN_UP_DATA),
                headers={
                    'content-type': 'application/json'
                })
        data = json.loads(response.get_data())
        print(data)
        self.assertEqual('success', data['status'])
        self.assertIn('login_token', data.keys())

    def test_users_endpoint_without_authorization(self):
        url = TestApiEndpoint.base_api_url + 'users'
        response = self.app_client.get(url, headers={
            'content-type': 'application/json',
        })
        data = json.loads(response.get_data())
        print(data)
        self.assertEqual('AUTHORIZATION_HEADER_ERROR', data['error_type'])

    def test_users_endpoint_with_authorization_but_not_type_bearer(self):
        url = TestApiEndpoint.base_api_url + 'users'
        response = self.app_client.get(url, headers={
            'content-type': 'application/json',
            'Authorization': 'bgjkbjsblknesklkenrknfnekwnlfklwneflkdnsknewkdsflkendlfnkle'
        })
        data = json.loads(response.get_data())
        print(data)
        self.assertEqual('AUTHORIZATION_HEADER_ERROR', data['error_type'])
        self.assertEqual(data['message'], 'Authorization type must be Bearer Token')