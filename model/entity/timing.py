from sqlalchemy.orm import relationship
from model.entity.base import Base
from sqlalchemy import Column, Integer, Time, Date, ForeignKey


class Timing(Base):
    __tablename__ = "timing_tbl"
    id = Column(Integer, primary_key=True)
    timing_date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    doctor_id = Column(Integer, ForeignKey("doctor_tbl.id"))
    doctor = relationship("Doctor")

    def __init__(self, timing_date, start_time, end_time, doctor):
        self.timing_date = timing_date
        self.start_time = start_time
        self.end_time = end_time
        self.doctor = doctor

