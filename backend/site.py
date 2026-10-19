import os
import threading
import webbrowser
from flask import Flask
from flask_cors import CORS

from config import API_URL_PREFIX
from auth.auth_controller import auth_bp
from data.data_controller import data_bp
from controllers.frontend_controller import frontend_bp


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(auth_bp, url_prefix=API_URL_PREFIX)
    app.register_blueprint(data_bp, url_prefix=API_URL_PREFIX)

    app.register_blueprint(frontend_bp)

    return app


if __name__ == '__main__':
    app = create_app()

    print('--- СЕРВЕР ЗАПУЩЕН ---')
    print('Откройте в браузере: http://127.0.0.1:5000')
    
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        threading.Timer(1.0, lambda: webbrowser.open_new("http://127.0.0.1:5000")).start()

    app.run(host='127.0.0.1', port=5000, debug=True)