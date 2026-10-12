from repositories.data_repository import DataRepository


class DataService:
    def __init__(self):
        self.data_repo = DataRepository()

    def get_protected_data(self):
        return self.data_repo.get_dashboard_data()