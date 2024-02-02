from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base


class Doctor(Base):
    __tablename__ = "doctor_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    national_id = Column(String(15))
    date_birth = Column(DateTime)
    phone_number = Column(String(15))
    username = Column(String(30))
    password = Column(String(30))
    skill = Column(String(50))
    medical_service_id = Column(Integer, ForeignKey("medical_service_tbl.id"))
    status = Column(Boolean)

    medical_service = relationship("MedicalService")

    def __init__(self, name, family, national_id, date_birth, phone_number, username, password, skill, medical_service,
                 status=True):
        self.id = None
        self.id = None
        self.name = name
        self.family = family
        self.national_id = national_id
        self.date_birth = date_birth
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.status = status
        self.skill = skill
        self.medical_service = medical_service
