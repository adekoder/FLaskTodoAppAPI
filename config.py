import os 

base_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig():
    pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'This is a dev secret key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://adekoder:adekoder@localhost/flask-todo-api'

class TestingConfig(BaseConfig):
    TESTING = True
    SECRET_KEY = 'This is a dev secret key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
            os.path.join(base_dir, 'test.db')
    WTF_CSRF_ENABLED = False



config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}