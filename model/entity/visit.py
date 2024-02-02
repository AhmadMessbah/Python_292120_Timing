from sqlalchemy import Column, Integer, String, ForeignKey

from model.entity.base import Base


class Visit(Base):
    __tablename__ = "visit_tbl"
    id = Column(Integer, primary_key=True)
    patient = Column(Integer, ForeignKey("patient_tbl.id"))
    timing = Column(String(30))
    visit_time = Column(String(20))
    duration = Column(String(20))
    payment = Column(String(20))

    def __init__(self, patient, timing, visit_time, duration, payment):
        self.patient = patient
        self.timing = timing
        self.visit_time = visit_time
        self.duration = duration
        self.payment = payment
