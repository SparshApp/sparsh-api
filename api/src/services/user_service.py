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

    def get_user(user_id):
        # user_data = None  # TODO: Retrieve user data from the 'users' table
        # return User.from_dict(user_data)
        return User.get_by_id(user_id)

    def update_user(self, user_id, name, email):
        pass
