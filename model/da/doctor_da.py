from model.da.database_manager import DatabaseManager
from model.entity.doctor import Doctor


class DoctorDa(DatabaseManager):
    def find_by_national_id(self, national_id):
        self.make_engine()
        entity = self.session.query().filter_by(national_id=national_id)
        return entity

    def find_by_username_password(self, username, password):
        self.make_engine()
        entity = self.session.query().filter_by(username_password=username - password)
        return entity

    def find_by_username(self, username):
        self.make_engine()
        entity = self.session.query().filter_by(username=username)
        return entity

    def find_by_family(self, family):
        self.make_engine()
        entity = self.session.query().filter_by(family=family)
        return entity

    def find_all(self, **kwargs):
        pass
