from sqlalchemy import Column, Integer, String

from model.entity.base import Base


class Visit(Base):
    __tablename__ = "visit_tbl"

    patient = Column(Integer(30))
    timing = Column(String(20))
    visit_time = Column(String(20))
    duration = Column(String(20))
    payment = Column(String(20))

    def __init__(self, patient, timing, visit_time, duration, payment):
        self.patient = patient
        self.timing = timing
        self.visit_time = visit_time
        self.duration = duration
        self.payment = payment

    def __repr__(self):
        return str(self.__dict__)
