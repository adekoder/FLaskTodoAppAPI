from app.model.user import User
from app.model.auth_token import AuthToken
from app.api.resource_schema import authentication_error_schema, successfull_login_schema, successfull_operation_schema
from .jwt import JsonWebToken

class Authentication():

    def __init__(self, request):
        self.__data = request.json
        self.email = self.__data['email']
        self.password = self.__data['password']
    
    def verify_login_credentials(self):
        self.user = User.query.filter_by(email=self.email).first()
        if self.user and self.user.verify_password(self.password):
            return True
        return False

    def login(self):
        if self.verify_login_credentials():
            json_web_token = JsonWebToken(self.user)
            token = json_web_token.generate_token()
            return successfull_login_schema(message='login successfull', token=token)
        return authentication_error_schema(message='Invalid login credentials')

    @staticmethod
    def auto_login(user):
        json_web_token = JsonWebToken(user)
        token = json_web_token.generate_token()
        return successfull_login_schema(message='User created and logged in', token=token)

    @staticmethod
    def logout_user(user_id):
        auth_token = AuthToken.query.filter_by(user_id=user_id).first()
        auth_token.delete()
        return successfull_operation_schema('LOGOUT_USER', 'Logout operation successfull')