from app import app
from app.controllers.task_controller import TaskController

@app.route('/task/create', methods=['POST'])
def create_task():
    return TaskController.create_task()

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    return TaskController.get_all_tasks()

@app.route('/task/<int:id>', methods=['GET'])
def get_task_by_id(id):
    return TaskController.get_task_by_id(id)

@app.route('/task/update/<int:id>', methods=['PUT'])
def update_task(id):
    return TaskController.update_task(id)

@app.route('/task/delete/<int:id>', methods=['DELETE'])
def delete_task(id):
    return TaskController.delete_task(id)