from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from model.entity.base import Base


class Patient(Base):
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
    visits = relationship("Visit", back_populates="patient", cascade="all, delete-orphan")

    def __init__(self, name, family, national_id, date_birth, phone_number, username, password,status=True):
        self.id = None
        self.name = name
        self.family = family
        self.national_id = national_id
        self.date_birth = date_birth
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.status = status
