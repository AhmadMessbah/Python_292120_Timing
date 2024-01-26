from sqlalchemy import Column, Integer, String,Boolean

class Timing:
    __tablename__ = "timing_tbl"
    id = Column(Integer, primary_key=True)
    timing_date = Column(String(30))
    start_time = Column(String(30))
    end_time = Column(String(10))


    def __init__(self, timing_date, start_time, end_time):
        self.timing_date = timing_date
        self.start_time = start_time
        self.end_time = end_time
        self.id = None

    def __repr__(self):
        return str(self.__dict__)
