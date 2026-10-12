from werkzeug.security import check_password_hash
from config import SECRET_TOKEN
from repositories.user_repository import UserRepository


class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def authenticate(self, username, password):
        if not username or not password:
            return None

        user = self.user_repo.find_by_username(username)
        if not user:
            return None

        if not check_password_hash(user['password_hash'], password):
            return None

        return SECRET_TOKEN

    def validate_token(self, auth_header):
        if not auth_header:
            return False
        return auth_header == f'Bearer {SECRET_TOKEN}'