from  flask import jsonify, request, make_response
from . import api


@api.route('/index')
def index():
    return 'index'

