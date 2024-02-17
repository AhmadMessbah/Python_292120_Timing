
from model.da.doctor_da import DoctorDa


da = DoctorDa()
result = da.find_by_username_and_password("aaa","Aa1234678$")
print(result)


