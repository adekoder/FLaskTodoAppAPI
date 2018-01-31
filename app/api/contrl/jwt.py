from datetime import datetime, timedelta
import jwt
from flask import current_app
from app.model.auth_token import AuthToken

class JsonWebToken():

    def __init__(self, user):
        self.user = user
        self.user_id = self.user.user_id
        self.auth_token = AuthToken()

    def create_jwt(self):
        payload =  {
            'user_id': self.user_id,
            'username': self.user.username,
            'email': self.user.email,
            'exp':self.token_exp
        }
        self.token = jwt.encode(payload, 
                current_app.config['SECRET_KEY'],
                algorithm='HS256')
    
    def generate_token(self, exp=3600):
        self.token_exp = datetime.utcnow() + timedelta(seconds=exp)
        self.create_jwt()
        if self.user_have_token():
            self.update_user_token()
        else:
            self.store_new_user_token()
        return self.token
        
    
    def user_have_token(self):
        return self.auth_token.query.filter_by(user_id=self.user_id).first()

    def update_user_token(self):
        user_token = self.auth_token.query.filter_by(user_id=self.user_id)
        user_token.token = self.token
        user_token.save()
    
    def store_new_user_token(self):
        self.auth_token.user_id = self.user_id
        self.auth_token.token = self.token
        self.auth_token.save()