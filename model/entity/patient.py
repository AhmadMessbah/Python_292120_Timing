from model.entity.user import User


class Patient(User):
    def __init__(self, name, family, national_id, date_birth, phone_number, username, password, status=True):
        super().__init__(name, family, national_id, date_birth, phone_number, username, password, status=True)
        self.id = None
