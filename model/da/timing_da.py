from model.da.database_manager import DatabaseManager
from model.entity.timing import Timing


class TimingDa(DatabaseManager):
    def find_by_date(self, date):
        self.make_engine()
        entity = self.session.query(Timing).filter(Timing.timing_date == date).all()
        return entity

    def find_by_start_time(self, start_time):
        self.make_engine()
        entity = self.session.query(Timing).filter(Timing.start_time == start_time).all()
        return entity

    def find_by_end_time(self, end_time):
        self.make_engine()
        entity = self.session.query(Timing).filter(Timing.end_time == end_time).all()
        return entity

    def find_by_doctor_id(self, doctor_id):
        self.make_engine()
        entity = self.session.query(Timing).filter(Timing.doctor_id == doctor_id).all()
        return entity

    def find_by_medical_id(self, doctor_id):
        self.make_engine()
        entity = self.session.query(Timing).filter(Timing.medical_id == doctor_id)
        return entity
