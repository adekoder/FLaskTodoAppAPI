import os 

base_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig():
    pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'This is a dev secret key'
    SQLALCHEMY_DATABASE_URL = 'sqlite:///' + \
            os.path.join(base_dir, 'todo_list.db')

class TestingConfig(BaseConfig):
    TESTING = True
    SECRET_KEY = 'This is a dev secret key'
    SQLALCHEMY_DATABASE_URL = 'sqlite:///' + \
            os.path.join(base_dir, 'test.db')



config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}