from app import app
from app.controllers.task_controller import TaskController

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    return TaskController.get_all_tasks()

@app.route('/task/<int:id>', methods=['GET'])
def get_task_by_id(id):
    return TaskController.get_task_by_id(id)

@app.route('/task/update/<int:id>', methods=['PUT'])
def update_task(id):
    return TaskController.update_task(id)