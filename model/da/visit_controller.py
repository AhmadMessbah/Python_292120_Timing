from Python_292120_Timing.model.da.visit_da import VisitDa
from Python_292120_Timing.model.entity.visit import Visit


class VisitController:
    def __init__(self):
        self.da = VisitDa()

    def save(self, patient, visit_time):
        try:
            visit = Visit(patient, visit_time)
            self.da.save(visit)
            return True
        except Exception as e:
            print(e)
            return False

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
