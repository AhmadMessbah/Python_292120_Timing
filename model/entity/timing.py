from model.entity.base import Base
from sqlalchemy import Column, Integer, DateTime, Date, ForeignKey

class Timing(Base):
    __tablename__ = "timing_tbl"
    id = Column(Integer, primary_key=True)
    timing_date = Column(Date)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    doctor = Column(Integer, ForeignKey("doctor_tbl.id"))



    def __init__(self,doctor, timing_date, start_time, end_time):
        self.doctor = doctor
        self.timing_date = timing_date
        self.start_time = start_time
        self.end_time = end_time
        self.id = None

    def __repr__(self):
        return str(self.__dict__)
