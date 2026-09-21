from flask import Flask, request, jsonify

app = Flask(__name__)

# Тестовые учётные данные
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"
SECRET_TOKEN = "my-super-secret-token-12345"


@app.route('/api/login', methods=['POST'])
def login():
    creds = request.get_json(silent=True) or {}
    username = creds.get('username')
    password = creds.get('password')

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return jsonify({'token': SECRET_TOKEN}), 200
    return jsonify({'error': 'Неверный логин или пароль'}), 401


@app.route('/api/data', methods=['GET'])
def get_data():
    auth_header = request.headers.get('Authorization')

    if auth_header != f'Bearer {SECRET_TOKEN}':
        return jsonify({'error': 'Доступ запрещен. Требуется авторизация.'}), 401

    return jsonify({
        'message': 'Привет от бэкенда! (Данные защищены)',
        'items': ['Python', 'JavaScript', 'HTTP-сервер', 'HTML', 'Авторизация']
    }), 200


if __name__ == '__main__':
    print('Сервер запущен на http://localhost:5000')
    print('Доступен эндпоинт: http://localhost:5000/api/data')
    print('Логин: admin, Пароль: password123')
    app.run(host='localhost', port=5000)