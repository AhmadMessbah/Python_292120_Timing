from model.da.doctor_da import DoctorDa
from model.entity.doctor import Doctor
from model.entity.medical_service import MedicalService
from model.entity.timing import Timing


med_service = MedicalService("jarahi", "sdfsdfsdfds")
doctor = Doctor("name", "family", 'national_id', None, "phone_number", "username", "password", "skill", med_service)
timing = Timing("2012-5-14", "2012-5-14", "2012-5-14")
da = DoctorDa()
da.save(doctor)
da.save(timing)