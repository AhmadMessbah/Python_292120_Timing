from controller.patient_controller import PatientController
from controller.visit_controller import VisitController
p_controller = PatientController()
v_controller = VisitController()

# patient = p_controller.find_by_id(1)
patient = p_controller.save_patient_controller("A", "b", "C", None,"A","a","a")
print(patient)
# controller.save()