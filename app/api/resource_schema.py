from flask import jsonify

def validation_error_schema(errors):
    return jsonify({
        'status': 'error',
        'error_type': 'VALIDATION_ERROR',
        'errors': errors
    }), 422


def authentication_error_schema(message=None):
    return jsonify({
        'status': 'error',
        'error_type': 'AUTHENTICATION_ERROR',
        'message': message
    }), 401

def successfull_operation_schema(operation_type, message):
    return jsonify({
        'status': 'success',
        'operation_type': operation_type,
        'message': message,
    }), 200

def successfull_login_schema(message, token):
    return jsonify({
        'status': 'success',
        'operation_type': 'LOGIN',
        'message': message,
        'login_token': token.decode()
    }), 200

def header_error_schema(error_type, message):
    return jsonify({
        'status': 'error',
        'error_type': error_type,
        'message': message
    }), 401

def authorization_error_schema(message):
    return jsonify({
        'status': 'error',
        'error_type': 'AUTHORIZATION_ERROR',
        'message': message
    }), 401