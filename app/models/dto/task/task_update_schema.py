from marshmallow import Schema, fields, validate

class TaskUpdateSchema(Schema):
        description = fields.String(required=True, validate=validate.Length(max=100))