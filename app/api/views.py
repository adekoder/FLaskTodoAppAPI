from  flask import jsonify, request, make_response
from . import api


@api.route('/login', methods=['POST'])
def login():
    pass

@api.route('/signup', methods=['POST'])
def sign_up():
    pass 

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



