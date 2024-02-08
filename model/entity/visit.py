from sqlalchemy import Column, Integer, String, ForeignKey

from model.entity.base import Base


class Visit(Base):
    __tablename__ = "visit_tbl"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patient_tbl.id"))
    timing_id = Column(Integer, ForeignKey("timing_tbl.id"))
    visit_time = Column(String(20))
    duration = Column(String(20))
    payment = Column(String(20))

    def __init__(self, patient_id, timing_id, visit_time, duration, payment):
        self.patient_id = patient_id
        self.timing_id = timing_id
        self.visit_time = visit_time
        self.duration = duration
        self.payment = payment
