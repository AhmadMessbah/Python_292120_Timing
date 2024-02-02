from controller.medical_service_controller import MedicalServiceController
from model.da.database_manager import DatabaseManager
from model.da.doctor_da import DoctorDa
from model.da.medical_service_da import MedicalServiceDa
from model.entity.doctor import Doctor
from model.entity.medical_service import MedicalService
from model.entity.timing import Timing


med_service = MedicalService("jarahi", "sdfsdfsdfds")
# doctor = Doctor("name", "family", 'national_id', None, "phone_number", "username", "password", "skill", med_service)
# timing = Timing("2012-5-14", "2012-5-14", "2012-5-14")
# da = DoctorDa()
# da.save(doctor)
# da.save(timing)


# med_service = MedicalServiceController()
# med_service.edit(1, "TTTTTT", "DDDDDD")
#
# da = MedicalServiceDa()
# m = MedicalService("TTTTTT", "DDDDDD")
# m.id = 1
# m = da.find_by_id(MedicalService,1)
# m.title = "Medical Service"
# da.edit(m)
# medical = da.find_by_id(MedicalService, 1)
# print(m)