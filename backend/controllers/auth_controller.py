from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get('username')
    password = data.get('password')

    print(f"Попытка входа: {username}")

    token = auth_service.authenticate(username, password)

    if token:
        print("Успешный вход!")
        return jsonify({'token': token}), 200

    print("Неверный логин или пароль")
    return jsonify({'error': 'Неверный логин или пароль'}), 401