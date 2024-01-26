class Timing:
    def __init__(self, timing_date, start_time, end_time):
        self.timing_date = timing_date
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return str(self.__dict__)
