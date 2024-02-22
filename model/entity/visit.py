from sqlalchemy import Column, Integer, String, ForeignKey, Time
from sqlalchemy.orm import relationship
# from sqlalchemy.orm import relationship
from model.entity.base import Base


class Visit(Base):
    __tablename__ = "visit_tbl"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patient_tbl.id"), nullable="True")
    patient = relationship ("Patient")

    timing_id = Column(Integer, ForeignKey("timing_tbl.id"), nullable="True")
    timing = relationship("Timing")
    visit_time = Column(Time)
    duration = Column(String(20))
    payment = Column(String(20))

    def __init__(self, patient, timing, visit_time, duration, payment):
        self.patient = patient
        self.timing = timing
        self.visit_time = visit_time
        self.duration = duration
        self.payment = payment
