from test import BaseAppApiTest
from app.api.utilities import generate_random_string

class TestUtilitiesFunction(BaseAppApiTest):

    def test_generate_random_string(self):
        string = generate_random_string()
        print(string)
        self.assertNotEqual(None, string)

    def test_if_generate_random_string_generate_unique_strings(self):
        string1 = generate_random_string()
        string2 = generate_random_string()
        self.assertNotEqual(string1, string2)

    def test_if_generate_random_string_return_specified_size(self):
        size = 5
        string = generate_random_string(size)
        self.assertEqual(size, len(string))
