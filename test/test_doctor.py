from controller.medical_service_controller import MedicalServiceController
from controller.patient_controller import PatientController
from model.da.database_manager import DatabaseManager
from model.da.doctor_da import DoctorDa
from model.da.medical_service_da import MedicalServiceDa
from model.entity.doctor import Doctor
from model.entity.medical_service import MedicalService
from model.entity.timing import Timing
from controller.doctor_controller import DoctorController

# save_medical
medical_service = MedicalServiceController()
medical = medical_service.save("aaaaaaa", "dhohsldw")
doc = DoctorController()
print(doc.save("aaaaaa", "fgDDerffgeD", "0123456789", "1400.12.12", "09123665487", "ammm", "Aa123456$", "jarahi",
               medical))
# print(doctor)
#
