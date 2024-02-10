from model.da.visit_da import VisitDa
from model.entity.visit import Visit


class VisitController:
    def __init__(self):
        self.da = VisitDa()

    def save(self, patient_id, timing_id, visit_time, duration, payment):
        try:
            visit = Visit(patient_id, timing_id, visit_time, duration, payment)
            self.da.save(visit)
            return True
        except Exception as e:
            return e

    def edit(self, id, patient, visit_time):
        try:
            visit = VisitDa(patient, visit_time)
            visit.id = id
            self.da.edit(visit)
            return True
        except Exception as e:
            return e

    def remove(self, id):
        try:
            self.da.remove(id)
            return "deleted"
        except Exception as e:
            return e

    def find_by_id(self, id):
        try:
            return self.da.find_by_id(id)
        except Exception as e:
            return e

    def find_by_timing_id(self, timing_id):
        try:
            return self.da.find_by_timing_id(timing_id)
        except Exception as e:
            return e

    def find_by_visit_time(self, visit_time):
        try:
            return self.da.find_by_visit_time(visit_time)
        except Exception as e:
            return e

    def find_by_patient_id(self, patient_id):
        try:
            return self.da.find_by_patient_id(patient_id)
        except Exception as e:
            return e
