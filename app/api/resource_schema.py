from flask import jsonify

def validation_error_schema(errors):
    print(errors)
    return jsonify({
        'status': 'error',
        'error_type': 'VALIDATION_ERROR',
        'errors': errors
    }), 422

