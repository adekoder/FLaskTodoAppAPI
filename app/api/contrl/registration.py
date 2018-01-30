from api.utilities import generate_random_string
from app.model.user import User

class Registration():
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


    def sigeUp(self):
        user = User()
        user.user_id = generate_random_string(10)
        user.username = self.username
        user.email = self.email
        user.password = self.password
        user.save()
