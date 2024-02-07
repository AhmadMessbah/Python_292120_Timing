from model.da.database_manager import DatabaseManager
from model.entity.medical_service import MedicalService


class MedicalServiceDa(DatabaseManager):
    def find_by_title(self, title):
        self.make_engine()
        entity = self.session.query(MedicalService).filter_by(MedicalService.title == title)
        return entity
