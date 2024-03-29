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
    status = Column(Boolean)
    timings = relationship("Timing", back_populates="doctor", cascade="all, delete-orphan")

    def __init__(self, name, family, national_id, date_birth, phone_number, username, password, skill,
                 status=True):
        self.name = name
        self.family = family
        self.national_id = national_id
        self.date_birth = date_birth
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.skill = skill
        self.status = status
