from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError

from app.models.db.db_model import User
from app.models.dto.user.user_schema import UserSchema
from app.models.dto.user.user_update_Schema import UserUpdateSchema
from app.tools.session_scope import session_scope


class UserController(Resource):
    # get one 
    
    # get all
    def get_all():
        with session_scope() as session:
            users = session.query(User).all()
            user_scheme = UserSchema(many=True)
            user_serialized = user_scheme.dump(users)
        return jsonify(user_serialized), 200
    
    # get by id
    
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