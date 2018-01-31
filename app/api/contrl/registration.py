from app.api.utilities import generate_random_string
from app.model.user import User
from .authentication import Authentication
class Registration():
    
    def __init__(self, request):
        self.__data = request.json
        self.username = self.__data['username']
        self.email = self.__data['email']
        self.password = self.__data['password']


    def create_user(self):
        self.user = User()
        self.user.user_id = generate_random_string(10)
        self.user.username = self.username
        self.user.email = self.email
        self.user.password = self.password
        self.user.save()
        return Authentication.auto_login(self.user)

