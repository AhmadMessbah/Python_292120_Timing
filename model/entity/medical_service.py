from sqlalchemy import Column, Integer, String,Boolean, DateTime
from model.entity.base import Base

class MedicalService(Base):
    __tablename__ = "medical_service_tbl"
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(255))

    def __init__(self, title, description):
        self.title = title
        self.description = description
