from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError

from app.models.db.db_model import Task
from app.models.dto.task.task_schema import TaskSchema
from app.models.dto.task.task_update_schema import TaskUpdateSchema
from app.tools.session_scope import session_scope


class TaskController(Resource):
    # Create
    def create_task():
        task_schema = TaskSchema()
        try:
            data = task_schema.load(request.json)
        except ValidationError as e:
            return jsonify(e.messages), 400
        
        with session_scope() as session:
            task = Task(**data)
            session.add(task)
            session.commit()
            task_serialized = task_schema.dump(task)
        return jsonify(task_serialized), 201

    # get all
    def get_all_tasks():
        with session_scope() as session:
            tasks = session.query(Task).all()
            task_schema = TaskSchema(many=True)
            task_serialized = task_schema.dump(tasks)
        return jsonify(task_serialized), 200
    
    # get by id
    def get_task_by_id(id):
        with session_scope() as session:
            task = session.get(Task, id)
            if task is None:
                return jsonify({"erreur" : "Tâche introuvable"}), 404
            task_schema = TaskSchema(many=False)
            task_serialized = task_schema.dump(task)
        return jsonify(task_serialized), 200

    # Update
    def update_task(id):
        task_schema = TaskUpdateSchema()
        try:
            data = task_schema.load(request.json, partial=True)
        except ValidationError as e:
            return jsonify(e.messages), 400
        
        with session_scope() as session:
            task = session.query(Task).filter_by(id=id).first()
            if task:
                for key, values in data.items():
                    setattr(task, key, values)
                task_serialized = task_schema.dump(task)
                return jsonify(task_serialized), 200
            else:
                return {'message' : f'Aucune tâche trouvé avec id : {id}'}, 404

    # Delete
    def delete_user(id):
        with session_scope() as session:
            task = session.query(Task).filter_by(id=id).first()
            if task:
                session.delete(task)
                return jsonify({"message": "Tâche supprimée avec succès"}), 200
            else:
                return jsonify({"message": f"Aucune tâche trouvée avec id : {id}"}), 404