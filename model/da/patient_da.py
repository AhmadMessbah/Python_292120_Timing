from model.da.database_manager import DatabaseManager
from model.entity.patient import Patient


class PatientDa(DatabaseManager):

    def find_by_family(self, family):
        self.make_engine()
        entity = self.session.query(Patient).filter(Patient.family == family)
        self.session.refresh(entity)
        self.session.close()
        return entity

    def find_by_national_id(self, national_id):
        self.make_engine()
        entity = self.session.query(Patient).filter_by(national_id=national_id)
        return entity

    def find_by_username(self, username):
        self.make_engine()
        entity = self.session.query(Patient).filter_by(username=username)
        return entity

    def find_by_username_password(self, username, password):
        self.make_engine()
        entity = self.session.query(Patient).filter_by(username=username, password=password)
        return entity

    def find_by_username_and_password(self, username, password):
        self.make_engine()
        entity = self.session.query(Patient).filter(
            (Patient.username == username, Patient.password == password))
        return entity
