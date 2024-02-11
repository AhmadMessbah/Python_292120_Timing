from controller.timing_controller import TimingController
from controller.visit_controller import VisitController
from controller.patient_controller import PatientController


patient = PatientController()
p1 = patient.find_by_id(3)
print(p1)

# timing = TimingController()
# t1 = timing.find_by_id(3)
# print(t1)
#
# da = VisitController()
# visit = da.save(p1,t1,"12:30","00:30","300000")
# print(visit)