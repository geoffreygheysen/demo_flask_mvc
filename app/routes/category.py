from app import app
from app.controllers.category_controller import CategoryController

# routes pour créer une categorie
@app.route('/category/create', methods=['POST'])
def create_category():
    return CategoryController.create_category()

# routes pour obtenir toutes les categories
@app.route('/categories', methods=['GET'])
def get_all_categories():
    return CategoryController.get_all_categories()

# routes pour obtenir une categorie par son id
@app.route('/category/<int:id>', methods=['GET'])
def get_category_by_id(id):
    return CategoryController.get_category_by_id(id)

# routes pour update une categorie
@app.route('/category/update/<int:id>', methods=['PUT'])
def update_category(id):
    return CategoryController.update_category(id)

# routes pour delete une categorie
@app.route('/category/delete/<int:id>', methods=['DELETE'])
def delete_category(id):
    return CategoryController.delete_category(id)