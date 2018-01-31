from flask import json
from test import BaseAppApiTest

base_api_url = 'api/v1/'

VALID_SIGN_UP_DATA = {
    'username': 'test123',
    'email': 'test@example.com',
    'password': 'Debb23'
}

class TestDecoratorsFunctions(BaseAppApiTest):

    def test_content_type_is_set(self):
        url = base_api_url + 'signup'
        response = self.app_client.post(url, 
                data=json.dumps(VALID_SIGN_UP_DATA),
                headers={
                    'content-type': 'application/json'
                })
        data = json.loads(response.get_data())
        self.assertNotIn('CONTENT_TYPE_ERROR', data.values())

    def test_content_type_is_not_set(self):
        url = base_api_url + 'signup'
        response = self.app_client.post(
            url,  data=json.dumps(VALID_SIGN_UP_DATA)
        )
        data = json.loads(response.get_data())
        print(data)
        self.assertEqual('CONTENT_TYPE_ERROR', data['error_type'])