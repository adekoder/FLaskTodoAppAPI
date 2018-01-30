from  flask import jsonify, request, make_response
from . import api
from .validators import *
from .resource_schema import validation_error_schema

@api.route('/login', methods=['POST'])
def login():
    pass

@api.route('/signup', methods=['POST'])
def sign_up():
    inputs = RegistrationValidator(request)
    if not inputs.validate():
        return validation_error_schema(inputs.errors)

    return jsonify(status=True)
    

@api.route('/user', methods=['GET'])
def users():
    pass 

@api.route('/user/<string:user_id>', methods=['GET'])
def get_user(user_id):
    pass

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



