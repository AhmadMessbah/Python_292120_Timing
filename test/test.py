from model.da.doctor_da import DoctorDa
from model.da.medical_service_da import MedicalServiceDa
from model.da.timing_da import TimingDa
from model.entity.doctor import Doctor
from model.entity.medical_service import MedicalService
from model.entity.timing import Timing


# med_da = MedicalServiceDa()
# med_service = MedicalService("jarahi", "sdfsdfsdfds")
# med_da.save(med_service)
#
doc_da = DoctorDa()
# doctor = Doctor("fahime", "family", 'national_id', None, "phone_number", "username", "password", "skill", med_service)
# med_da.save(doctor)

doctor = doc_da.find_by_id(Doctor, 3)

timing_da =  TimingDa()
timing = Timing(doctor, "2012-5-14", "08:00", "14:00")
timing_da.save(timing)