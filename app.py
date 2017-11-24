from flask import (
    Flask,
    Blueprint,
    render_template,
)


from routes.login import main as login_routes
from routes.books import main as books_routes
from routes.user import main as user_routes
# from routes.cart import main as cart_routes
# from routes.sell import main as sell_routes
from routes.order import main as order_routes
from routes.board import main as board_routes




def create_app():
    app = Flask(__name__)
    app.register_blueprint(login_routes, url_prefix='/login')
    app.register_blueprint(books_routes, url_prefix='/book')
    app.register_blueprint(user_routes, url_prefix='/user')
    # app.register_blueprint(cart_routes, url_prefix='/cart')
    # app.register_blueprint(sell_routes, url_prefix='/sell')
    app.register_blueprint(order_routes, url_prefix='/order')
    app.register_blueprint(board_routes, url_prefix='/board')


    return app


app = create_app()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=5050,
    )
    app.run(**config)
