# from controller.timing_controller import TimingController
# from controller.visit_controller import VisitController
# from controller.patient_controller import PatientController


# patient = PatientController()
# p1 = patient.find_by_id(3)
# print(p1)

# timing = TimingController()
# t1 = timing.find_by_id(3)
# print(t1)
#
# da = VisitController()
# visit = da.save(p1,t1,"12:30","00:30","300000")
# print(visit)

from controller.medical_service_controller import MedicalServiceController
from controller.doctor_controller import DoctorController
from controller.timing_controller import TimingController
from controller.patient_controller import PatientController
from controller.visit_controller import VisitController

medical = MedicalServiceController()
doctor = DoctorController()
timing = TimingController()
patient = PatientController()

medical_result = medical.save("jarah", "ghalb")
doctor_result = doctor.save("diba", "mahmoudi", "5874216938", "1341.05.11", "8756324589", "dibaaaa", "mahboob", "jarah",
                            medical_result)
timing_result = timing.save("1402.12.03", "8:30", "10:30", doctor_result)
patient_result = patient.save("hanie", "mehri", "5462713265", "1385.06.12", "09123658791", "haniii", "mehriii")
VisitController.save(patient_result, timing_result, "16:00", "sick", "50000")
