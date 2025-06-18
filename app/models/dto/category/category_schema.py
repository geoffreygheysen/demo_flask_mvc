from marshmallow import Schema, fields

class CategorySchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)