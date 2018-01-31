from datetime import datetime
import jwt
from jwt.exceptions import ExpiredSignatureError
from flask import request, current_app
from .resource_schema import header_error_schema, authorization_error_schema
from app.model.auth_token import AuthToken

def content_type_json(func):
    def wrapper(*args, **kwargs):
        if not request.headers['content-type'] == 'application/json':
            return header_error_schema('CONTENT_TYPE_ERROR',
                    'content_type must be set to application/json')
        return func(*args, **kwargs)
    return wrapper


def token_exist(token):
    auth_token = AuthToken.query.filter_by(token=token).first()
    if not  auth_token:
        return False
    return True

def clear_user_token_from_db(token):
    auth_token = AuthToken.query.filter_by(token=token).first()
    auth_token.delete()

def token_required(func):
    def inner_wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return header_error_schema('AUTHORIZATION_HEADER_ERROR',
                'Authorization header must be set')
        auth = request.headers['Authorization'].split()
        if 'Bearer' not in auth:
            return header_error_schema('AUTHORIZATION_HEADER_ERROR',
                    'Authorization type must be Bearer Token')
        token = auth[1]
        if not token_exist(token):
            return authorization_error_schema('Invalid Authorization token')
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        except ExpiredSignatureError:
            clear_user_token_from_db(token)
            return authorization_error_schema('Token has expired')
        else:
            current_user = payload
        return func(current_user, *args, **kwargs)
    return inner_wrapper

