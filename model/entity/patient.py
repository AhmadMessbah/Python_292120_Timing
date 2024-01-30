from sqlalchemy import Column, Integer, String, Boolean

from model.entity.base import Base
from model.entity.user import User


class Patient(User, Base):
    __tablename__ = 'patient_tbl'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    national_id = Column(String(10))
    date_birth = Column(String(30))
    phone_number = Column(String(15))
    username = Column(String(30))
    password = Column(String(30))
    status = Column(Boolean)

    def __init__(self, name, family, national_id, date_birth, phone_number, username, password, status=True):
        super().__init__(name, family, national_id, date_birth, phone_number, username, password, status=True)
        self.id = None
