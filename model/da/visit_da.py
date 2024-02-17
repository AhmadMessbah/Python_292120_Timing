from model.da.database_manager import *
from model.entity.visit import Visit


class VisitDa(DatabaseManager):
    def find_by_timing_id(self, timing_id):
        self.make_engine()
        result = self.session.query(Visit).filter(Visit.timing_id == timing_id).all()
        return result

    def find_by_visit_time(self, visit_time):
        self.make_engine()
        result = self.session.query(Visit).filter(Visit.visit_time == visit_time).all()
        return result

    def find_by_patient_id(self, patient_id):
        self.make_engine()
        result = self.session.query(Visit).filter(Visit.patient_id == patient_id).all()
        return result
