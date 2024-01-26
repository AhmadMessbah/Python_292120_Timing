from model.entity.user import User


class Doctor(User):
    def __init__(self,name, family, national_id, date_birth, phone_number, username, password, skill, medical_service, status=True):
        super().__init__(name, family, national_id, date_birth, phone_number, username, password, status)
        self.skill = skill
        self.medical_service = medical_service
        self.id = None

