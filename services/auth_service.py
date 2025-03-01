from controllers.user_controller import UserController
from database.connection import Database


class AuthService:
    def __init__(self):
        db = Database()
        self.repository = UserController(db)

    def login(self, email, password):
        return self.repository.login_api(email, password)

    def register(self, user):
        return self.repository.register_api(user)