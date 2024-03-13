from flask import jsonify

from models.user import User
from models.user_model import user, db

class UserRepository:
    def __init__(self):
        self.users = {}

    def create_user(self, id, username, email):
        user = User(id, username, email)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User added successfully'}), 201

    def get_user(self, id):
        return self.users.get(id)

    def update_user(self, id, username=None, email=None):
        user = self.get_user(id)
        if user:
            if username:
                user.username = username
            if email:
                user.email = email
            return user
        return None

    def delete_user(self, id):
        return self.users.pop(id, None)

    def get_all_users(self):
        return user.query.all()
