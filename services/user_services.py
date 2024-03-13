from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, id, username, email):
        return self.user_repository.create_user(id, username, email)

    def get_user(self, id):
        return self.user_repository.get_user(id)

    def update_user(self, id, username=None, email=None):
        return self.user_repository.update_user(id, username, email)

    def delete_user(self, id):
        return self.user_repository.delete_user(id)

    def get_all_users(self):
        return self.user_repository.get_all_users()
