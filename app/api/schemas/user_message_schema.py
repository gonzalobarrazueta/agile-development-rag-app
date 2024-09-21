from marshmallow import Schema, fields


class UserMessageSchema(Schema):
    system_message = fields.Str(required=False)
    user_message = fields.Str(required=True)
