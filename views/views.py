from flask import Flask, request, jsonify, abort
from services.user_services import UserService
from models.user_model import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
user_service = UserService()


@app.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = user_service.get_all_users()
        if not users:
            return jsonify([])  # Return an empty list if there are no users
        user_list = []
        for user in users:
            user_dict = {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
            user_list.append(user_dict)
        return jsonify(user_list)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        abort(500)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    return jsonify(user.__dict__) if user else ('User not found', 404)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = user_service.create_user(data['id'], data['username'], data['email'])
    return jsonify(user.__dict__), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = user_service.update_user(user_id, data.get('username'), data.get('email'))
    return jsonify(user.__dict__) if user else ('User not found', 404)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = user_service.delete_user(user_id)
    return ('', 204) if result else ('User not found', 404)

if __name__ == '__main__':
    app.run(debug=True)
