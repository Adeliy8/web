class DataRepository:
    """Репозиторий защищённых данных."""

    def get_dashboard_data(self):
        return {
            'message': 'Привет от бэкенда!',
            'items': ['Python', 'JavaScript', 'HTTP-сервер', 'HTML', 'Авторизация']
        }