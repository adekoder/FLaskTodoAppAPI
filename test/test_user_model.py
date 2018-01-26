from test import User, BaseAppApiTest


class UserModelTest(BaseAppApiTest):

    def test_user_model(self):
        user = User()
        user.user_id = '144432'
        user.username = 'test'
        user.email = 'test@example.com'
        user.password = 'testpasswordrandomstring'
        self.assertEqual(None, user.save())
