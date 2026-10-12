from flask import Flask
from flask_cors import CORS

from config import API_URL_PREFIX
from controllers.auth_controller import auth_bp
from controllers.data_controller import data_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(auth_bp, url_prefix=API_URL_PREFIX)
    app.register_blueprint(data_bp, url_prefix=API_URL_PREFIX)
    return app


if __name__ == '__main__':
    app = create_app()
    print('--- СЕРВЕР ЗАПУЩЕН ---')
    print('Ссылка: http://127.0.0.1:5000')
    app.run(host='127.0.0.1', port=5000, debug=True)