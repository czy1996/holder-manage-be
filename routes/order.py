from flask import (
    Blueprint,
    request,
    jsonify,
)
from models.book import Book
from models.order import Order

from utils import log, json_response

import datetime

main = Blueprint('order', __name__)


@main.route('/get')
def get_orders():
    l = Order.all()
    l = [o.json() for o in l]
    l.reverse()
    for order in l:
        r = []
        for id, q in order['items'].items():
            # log(id, q)
            title = Book.get(int(id)).title
            r.append({
                'title': title,
                'quantity': q,
            })
        order['items'] = r
        order['time'] = datetime.datetime.fromtimestamp(order['ct']).strftime("%Y-%m-%d %H:%M:%S")
    return json_response(l)


@main.route('/update', methods=['POST'])
def update_orders():
    data = request.get_json()
    order_id = data.pop('id')
    o = Order.get(order_id)
    o.update(data)
    return json_response(o.json())
