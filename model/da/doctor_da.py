from model.da.database_manager import *
from model.entity.doctor import Doctor


class DoctorDa(DatabaseManager):
    def find_by_national_id(self, national_id):
        self.make_engine()
        entity = self.session.query().filter_by(Doctor.national_id == national_id).all()
        return entity

    def find_by_family(self, family):
        self.make_engine()
        entity = self.session.query().filter_by(Doctor.family == family).all()
        return entity

    def find_by_username_and_password(self, username, password):
        self.make_engine()
        entity = self.session.query(Doctor).filter(
            and_((Doctor.username == username, Doctor.password == password))).all()
        return entity
