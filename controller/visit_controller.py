from model.da.visit_da import VisitDa
from model.entity.visit import Visit


class VisitController:
    @classmethod
    def save(cls, patient, timing, visit_time, duration, payment):
        try:
            visit = Visit(patient, timing, visit_time, duration, payment)
            da = VisitDa()
            da.save(visit)
            return visit
        except Exception as e:
            return e

    @classmethod
    def edit(cls, id, visit_time, duration, payment):
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

    @classmethod
    def remove(cls, id):
        try:
            da = VisitDa()
            da.remove(id)
            return "deleted"
        except Exception as e:
            return e

    @classmethod
    def find_by_id(cls, id):
        try:
            da = VisitDa()
            return da.find_by_id(id)
        except Exception as e:
            return e

    @classmethod
    def find_by_timing_id(cls, timing_id):
        try:
            da = VisitDa()
            return da.find_by_timing_id(timing_id)
        except Exception as e:
            return e

    @classmethod
    def find_by_visit_time(cls, visit_time):
        try:
            da = VisitDa()
            return da.find_by_visit_time(visit_time)
        except Exception as e:
            return e

    @classmethod
    def find_by_patient_id(cls, patient_id):
        try:
            da = VisitDa()
            return da.find_by_patient_id(patient_id)
        except Exception as e:
            return e
