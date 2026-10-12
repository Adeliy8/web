from werkzeug.security import generate_password_hash

class UserRepository:
    """Репозиторий пользователей (в будущем можно заменить на БД)."""

    def __init__(self):
        self._users = {
            "admin": {
                "username": "admin",
                "password_hash": generate_password_hash("password123", method='pbkdf2:sha256')
            }
        }

    def find_by_username(self, username):
        return self._users.get(username)