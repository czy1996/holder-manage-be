from flask import (
    Blueprint,
    request,
    jsonify,
    make_response
)
from models.Board import Board

from utils import log, json_response

main = Blueprint('board', __name__)


@main.route('/get')
def get():
    """

    :return: 
    """
    args = request.args
    bid = int(args.get('id'))
    b = Board.find_one(id=bid)
    # log('get board', b.json())
    return json_response(b.json())


@main.route('/update', methods=['POST'])
def check():
    data = request.get_json()
    board_id = data.get('id')
    b = Board.get(board_id)
    b.update({'content': data.get('content')})
    return jsonify(status='ok')

