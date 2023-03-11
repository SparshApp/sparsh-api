import uuid
from models import User


class UserService:

    def create_user(self, name, email):
        user_id = str(uuid.uuid4())
        user = User(user_id, name, email)
        user.save()
        return user

    def get_users(self):
        return User.get_all()

    def get_user(self, user_id):
        return User.get_by_id(user_id)

    def update_user(self, user_id, name, email):
        pass
