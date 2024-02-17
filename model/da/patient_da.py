from model.da.database_manager import *
from model.entity.patient import Patient

class PatientDa(DatabaseManager):
    def find_by_family(self, family):
        self.make_engine()
        entity = self.session.query(Patient).filter(Patient.family == family).all()
        self.session.refresh(entity)
        self.session.close()
        return entity

    def find_by_national_id(self, national_id):
        self.make_engine()
        entity = self.session.query(Patient).filter(Patient.national_id == national_id).all()
        return entity

    def find_by_username(self, username):
        self.make_engine()
        entity = self.session.query(Patient).filter(Patient.username == username).all()
        return entity

    def find_by_username_and_password(self, username, password):
        self.make_engine()
        entity = self.session.query(Patient).filter(
            and_(Patient.username == username, Patient.password == password)).all()
        return entity
