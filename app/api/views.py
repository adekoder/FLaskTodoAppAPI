from  flask import jsonify, request, make_response
from . import api
from .validators import *
from .resource_schema import validation_error_schema, header_error_schema
from .contrl.registration import Registration
from .decorators import token_required


@api.before_request
def content_type_json():
    if not request.headers['content-type'] == 'application/json':
        return header_error_schema('CONTENT_TYPE_ERROR',
                'content_type must be set to application/json')

@api.route('/login', methods=['POST'])
def login():
    pass

@api.route('/signup', methods=['POST'])
def sign_up():
    inputs = RegistrationValidator(request)
    if not inputs.validate():
        return validation_error_schema(inputs.errors)
    registration = Registration(request)
    return registration.create_user()

@api.route('/users', methods=['GET'])
def users():
    pass

@api.route('/user/<string:user_id>', methods=['GET'])
@token_required
def get_user(current_user, user_id):
    return jsonify(current_user)

@api.route('/user/todo', methods=['GET'])
def get_user_todo():
    pass

@api.route('/user/todo', methods=['POST'])
def create_todo():
    pass

@api.route('/user/todo/todo_id', methods=['PUT'])
def update_todo_status():
    pass

@api.route('/user/todo/todo_id', methods=['DELETE'])
def delete_todo_item():
    pass



