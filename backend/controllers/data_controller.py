from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from services.data_service import DataService

data_bp = Blueprint('data', __name__)
auth_service = AuthService()
data_service = DataService()


@data_bp.route('/data', methods=['GET'])
def get_data():
    auth_header = request.headers.get('Authorization')

    if not auth_service.validate_token(auth_header):
        return jsonify({'error': 'Доступ запрещен'}), 401

    return jsonify(data_service.get_protected_data()), 200