from controller.doctor_controller import DoctorController
from controller.medical_service_controller import MedicalServiceController
from controller.timing_controller import TimingController
from model.da.database_manager import DatabaseManager
from model.da.doctor_da import DoctorDa
from model.da.timing_da import TimingDa
from model.entity.doctor import Doctor
from model.entity.timing import Timing
# save_timing
# medic = MedicalServiceController()
# result = medic.save("amal","sioduhfv9ow")
# print(result)
# da= DoctorController()
# doctor = da.save("asghar","bbb","0123456789","1400.10.10","09123339666","doc","Aa123456$","jarahi",result)
# print(doctor)
# timing = TimingController()
# t1 = timing.save("1402.12.3", "8:30", "10:30",doctor)
# print(t1)
#

# remove_timing
timing = TimingController()
t1 = timing.remove(2)
print(t1)

# edit_timing
# timing = TimingController()
# t1 = timing.edit("1402.12.3","10:20","11:10","")
# print(t1)

# find_by_doctor_id
# timing = TimingController()
# t1 = timing.find_by_doctor_id(1)
# print(t1)


# find_by_date
# timing = TimingController()
# t1 = timing.find_by_date(1)
# print(t1)

# find_by_start_time
# timing = TimingController()
# t1 = timing.find_by_start_time(1)
# print(t1)

# find_by_end_time
# timing = TimingController()
# t1 = timing.find_by_end_time(1)
# print(t1)