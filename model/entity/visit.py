class Visit:
    def __init__(self, patient, timing, visit_time, duration, payment):
        self.id = None
        self.patient = patient
        self.timing = timing
        self.visit_time = visit_time
        self.duration = duration
        self.payment = payment

    def __repr__(self):
        return str(self.__dict__)