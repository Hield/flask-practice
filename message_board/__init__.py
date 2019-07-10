from flask import Flask
from flask_cors import CORS
from message_board.controller import message

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    app.register_blueprint(message.bp)

    return app