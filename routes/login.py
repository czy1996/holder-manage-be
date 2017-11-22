from flask import (
    Blueprint,
    request,
    jsonify,
    make_response
)
from models.admin import Admin

from utils import log

main = Blueprint('login', __name__)


@main.route('', methods=['POST'])
def login():
    """
    
    :return: 
    """
    log(request.get_json(), type(request.get_json()))
    admin = Admin.find_one(name=request.get_json().get('name'))
    session_id = admin.validate_auth(request.get_json())
    if session_id is not None:
        response = jsonify({
            'status': 'ok',
            'name': request.get_json().get('name')
        })
        response.set_cookie('Session-id', session_id)
        response.headers['Access-Control-Allow-Credentials'] = 'true'
    else:
        response = jsonify({
            'status': 'fail',
        })
    return response


@main.route('/check')
def check():
    session_id = request.cookies.get('Session-id', None)
    response = jsonify({
        'status': 'fail',
    })
    if session_id is not None:
        log(session_id)
        if Admin.is_valid_login(session_id):
            response = jsonify({
                'status': 'ok',
                'name': Admin.current_admin().name,
            })

    return response
