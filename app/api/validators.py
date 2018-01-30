from flask_inputs import Inputs
from wtforms.validators import InputRequired, Email, Regexp, ValidationError
from app.model import User 

def email_exist(form, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('Email already in use')

PASSWORD_REGEX = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{4,8}$'
PASSWORD_ERROR_MESSAGE = 'Password must be at least 4 characters,\
    no more than 8 characters, and must include at least one upper case letter,\
    one lower case letter, and one numeric digit'

class RegistrationValidator(Inputs):

    json = {
        'username': [InputRequired(message='username not passed')],
        'email':  [InputRequired(), email_exist],
        'password': [
            InputRequired(),
            Regexp(PASSWORD_REGEX, message=PASSWORD_ERROR_MESSAGE)
            ]
    }
