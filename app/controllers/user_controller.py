from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError

from app.models.db.db_model import User
from app.models.dto.user.user_schema import UserSchema
from app.models.dto.user.user_update_Schema import UserUpdateSchema
from app.tools.session_scope import session_scope


class UserController(Resource):
    # Create
    def create_user():
        user_schema = UserSchema()
        try:
            data = user_schema.load(request.json)
        except ValidationError as e:
            return jsonify(e.messages), 400
        
        with session_scope() as session:
            user = User(**data)
            session.add(user)
            session.commit()
            user_serialized = user_schema.dump(user)
        return jsonify(user_serialized), 201
    
    # get all
    def get_all():
        with session_scope() as session:
            users = session.query(User).all()
            user_scheme = UserSchema(many=True)
            user_serialized = user_scheme.dump(users)
        return jsonify(user_serialized), 200
    
    # get by id
    def get_by_id(id):
        with session_scope() as session:
            user = session.get(User, id)
            if user is None:
                return jsonify({"erreur": "Utilisateur introuvable"}), 404
            user_scheme = UserSchema(many=False)
            user_serialized = user_scheme.dump(user)
        return jsonify(user_serialized), 200
    
    # get one by email
    def get_one_by_email(email):
        with session_scope() as session:
            user = session.query(User).filter_by(email=email).first()
            if user is None:
                return jsonify({"erreur": "Utilisateur non trouvé"}), 404
            user_scheme = UserSchema(many=False)
            user_serialized = user_scheme.dump(user)
        return jsonify(user_serialized), 200
    
    # update
    def update_email(id):
        user_schema = UserUpdateSchema()
        try:
            data = user_schema.load(request.json, partial=True)
        except ValidationError as e:
            return jsonify(e.messages), 400
        
        with session_scope() as session:
            user = session.query(User).filter_by(id=id).first()
            if user:
                for key, values in data.items():
                    setattr(user ,key, values)
                user_serialized = user_schema.dump(user)
                return jsonify(user_serialized), 200
            else:
                return {'message' : f'Aucun utilisateur trouvé avec id : {id}'}, 404
            
    # delete
    def delete_user(id):
        with session_scope() as session:
            user = session.get(User, id)
            if user is None:
                return jsonify({"erreur": "Utilisateur introuvable"}), 404
            user_schema = UserSchema()
            user_serialized = user_schema.dump(user)
            session.delete(user)
        return jsonify({"message": f"Utilisateur avec l'id {id} supprimé.", "user": user_serialized }), 200
