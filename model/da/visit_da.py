from Python_292120_Timing.model.da.database_manager import DatabaseManager
from Python_292120_Timing.model.entity.visit import Visit


class VisitDa(DatabaseManager):
    def find_by_timing_id(self, timing_id):
        self.make_engine()
        result = self.session.query(Visit).filter(Visit.timing_id == timing_id)
        return result

    def find_by_visit_time(self, visit_time):
        self.make_engine()
        result = self.session.query(Visit).filter(Visit.visit_time == visit_time)
        return result

    def find_by_patient_id(self, patient_id):
        self.make_engine()
        result = self.session.query(Visit).filter(Visit.patient_id == patient_id)
        return result
