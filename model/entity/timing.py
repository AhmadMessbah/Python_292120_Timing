from model.entity.base import Base
from sqlalchemy import Column, Integer, DateTime, Date

class Timing(Base):
    __tablename__ = "timing_tbl"
    id = Column(Integer, primary_key=True)
    timing_date = Column(Date)
    start_time = Column(DateTime)
    end_time = Column(DateTime)


    def __init__(self, timing_date, start_time, end_time):
        self.timing_date = timing_date
        self.start_time = start_time
        self.end_time = end_time
        self.id = None

    def __repr__(self):
        return str(self.__dict__)
