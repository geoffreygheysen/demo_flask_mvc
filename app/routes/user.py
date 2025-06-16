from app import app
from app.controllers.user_controller import UserController


@app.route('/users', methods=['GET'])
def get_all():
    return UserController.get_all()

@app.route('/user/<int:id>', methods=['PUT'])
def update_email(id):
    return UserController.update_email(id)