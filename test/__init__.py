import unittest
from app import create_app, db

class BaseAppApiTest(unittest.TestCase):

    def setUp(self):
        self.db = db
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app_client = self.app.test_client()
        self.db.create_all()
    
    def tearDown(self):
        self.db.drop_all()
        self.app_context.pop()
