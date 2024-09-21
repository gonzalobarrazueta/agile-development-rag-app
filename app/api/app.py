from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from .schemas.user_message_schema import UserMessageSchema
from app.rag.ragflow import chat

generate_route = Blueprint('generate_response', __name__)

user_message_schema = UserMessageSchema()


@generate_route.route('/generate', methods=['POST'])
def generate_response():
    try:
        data = user_message_schema.load(request.json)
    except ValidationError as e:
        return jsonify({'errors': e.messages}), 400

    system_message = data['system_message']
    user_message = data['user_message']

    sources, response = chat(system_message, user_message)

    chat_response = {
        "sources": sources,
        "response": response
    }

    return jsonify(chat_response)
