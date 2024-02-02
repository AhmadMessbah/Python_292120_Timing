from model.da.database_manager import DatabaseManager
from model.entity.patient import Patient


class MedicalServiceDa(DatabaseManager):
    def find_by_title(self, title):
        self.make_engine()
        entity = self.session.query(Patient).filter_by(title=title)
        return entity
