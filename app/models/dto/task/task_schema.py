from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.Integer(dump_only=True)
    description = fields.String(required=True)
    user_id = fields.Integer(required=True, allow_none=True)