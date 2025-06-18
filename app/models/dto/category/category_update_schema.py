from marshmallow import Schema, fields, validate

class CategoryUpdateSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(max=50))