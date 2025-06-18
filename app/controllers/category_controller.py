from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError

from app.models.db.db_model import Category
from app.models.dto.category.category_schema import CategorySchema
from app.tools.session_scope import session_scope


class CategoryController(Resource):
    #create
    def create_category():
        category_schema = CategorySchema()
        with session_scope() as session:
            try:
                data = category_schema.load(request.json)
            except ValidationError as e:
                return jsonify(e.messages), 400

            category = Category(**data)
            session.add(category)
            session.commit()
            category_serialized = category_schema.dump(category)
        return jsonify(category_serialized), 201

    # get all categories
    def get_all_categories():
        with session_scope() as session:
            categories = session.query(Category).all()
            category_schema = CategorySchema(many=True)
            category_serialized = category_schema.dump(categories)
        return jsonify(category_serialized), 200
    
    # get category by id
    def get_category_by_id(id):
        with session_scope() as session:
            category = session.get(Category, id)
            if category is None:
                return jsonify({"erreur": "Catégorie introuvable"}), 404
            category_schema = CategorySchema(many=False)
            category_serialized = category_schema.dump(category)
        return jsonify(category_serialized), 200
    
    # update category
    def update_category(id):
        category_schema = CategorySchema()
        with session_scope() as session:
            try:
                data = category_schema.load(request.json, partial=True)
            except ValidationError as e:
                return jsonify(e.messages), 400

            category = session.query(Category).filter_by(id=id).first()
            if category:
                for key, value in data.items():
                    setattr(category, key, value)
                session.commit()
                category_serialized = category_schema.dump(category)
                return jsonify(category_serialized), 200
            else:
                return jsonify({"erreur": "Catégorie introuvable"}), 404
    
    # delete category
    def delete_category(id):
        with session_scope() as session:
            category = session.get(Category, id)
            if category is None:
                return jsonify({"erreur": "Catégorie introuvable"}), 404
            session.delete(category)
            session.commit()
            return jsonify({"message": "Catégorie supprimée avec succès"}), 200