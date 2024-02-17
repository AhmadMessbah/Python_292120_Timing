from model.da.database_manager import *
from model.entity.medical_service import MedicalService


class MedicalServiceDa(DatabaseManager):
    # def find_by_titleee(self, title):
    #     self.make_engine()
    #     entity = self.session.query(MedicalService).filter(MedicalService.title == title)
    #     return entity
    def find_by_title_and_description(self, title, description):
        self.make_engine()
        entity = self.session.query(MedicalService).filter(
            and_(MedicalService.title == title, MedicalService.description == description)).all()
        return entity
