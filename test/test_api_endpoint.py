from flask import json
from test import BaseAppApiTest

INVALID_SIGN_UP_DATA = {
    'username': 'test123',
    'email': 'test@example.com',
    'password': '22332'
}

class TestApiEndpoint(BaseAppApiTest):

    base_api_url = 'api/v1/'

    def test_registration_endpoint_return_validtion_error(self):
        url = TestApiEndpoint.base_api_url + 'signup'
        response = self.app_client.post(url, data=json.dumps(INVALID_SIGN_UP_DATA),
                headers={
                    'content-type': 'application/json'
                })
        data = json.loads(response.get_data())
        self.assertEqual('error', data['status'])
        self.assertEqual('VALIDATION_ERROR', data['error_type'])