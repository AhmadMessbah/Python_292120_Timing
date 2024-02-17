from model.da.database_manager import DatabaseManager
from model.entity.timing import Timing


class TimingDa(DatabaseManager):
    def find_by_date(self, date):
        self.make_engine()
        entity = self.session.query(Timing).filter_by(date=date)
        return entity

    def find_by_start_time(self, start_time):
        self.make_engine()
        entity = self.session.query(Timing).filter_by(start_time=start_time)
        return entity

    def find_by_end_time(self, end_time):
        self.make_engine()
        entity = self.session.query(Timing).filter_by(end_time=end_time)
        return entity

    def find_by_doctor_id(self, doctor_id):
        self.make_engine()
        entity = self.session.query(Timing).filter_by(doctor_id=doctor_id)
        return entity

