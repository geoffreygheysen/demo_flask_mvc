from marshmallow import Schema, fields, validate

class UserUpdateSchema(Schema):
    email = fields.String(required=True, validate=validate.Length(max=100))