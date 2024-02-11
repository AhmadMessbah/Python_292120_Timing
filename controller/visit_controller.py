from model.da.visit_da import VisitDa
from model.entity.visit import Visit


class VisitController:
    def __init__(self):
        self.da = VisitDa()

    def save(self, patient, timing, visit_time, duration, payment):
        try:
            visit = Visit(patient, timing, visit_time, duration, payment)
            result = self.da.save(visit)
            if result:
                print(result)
        except Exception as e:
            return e

    def edit(self, id, visit_time,duration,payment):
        try:
            da = VisitDa()
            visit = da.find_by_id(Visit, id)

            if visit:
                visit.visit_time = visit_time
                visit.duration = duration
                visit.payment = payment
                result = da.edit(visit)
                print(result)

        except Exception as e:
            print(e)
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
