from app import app
from app.controllers.user_controller import UserController

@app.route('/user/create', methods=['POST'])
def create_user():
    return UserController.create_user()

@app.route('/users', methods=['GET'])
def get_users():
    return UserController.get_all()

@app.route('/user/<int:id>', methods=['GET'])
def get_by_id(id):
    return UserController.get_by_id(id)

@app.route('/user/email/<string:email>', methods=['GET'])
def get_one_by_email(email):
    return UserController.get_one_by_email(email)

@app.route('/user/<int:id>', methods=['PUT'])
def update_email(id):
    return UserController.update_email(id)

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    return UserController.delete_user(id)