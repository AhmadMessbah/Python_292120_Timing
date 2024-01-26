from model.da.doctor_da import DoctorDa
from model.entity.doctor import Doctor
from model.entity.medical_service import MedicalService

med_service = MedicalService("jarahi", "sdfsdfsdfds")
doctor = Doctor("name", "family", 'national_id', None, "phone_number", "username", "password", "skill", med_service)

da = DoctorDa()
da.save(doctor)