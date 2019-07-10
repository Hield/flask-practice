from flask import Flask
from flask_cors import CORS
from message_board.controller import message
from message_board.soap import create_soap_handler
from werkzeug.wsgi import DispatcherMiddleware

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    app.register_blueprint(message.bp)
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/soap': create_soap_handler()
    })

    return app