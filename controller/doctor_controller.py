from model.da.doctor_da import DoctorDa
from model.entity.doctor import Doctor

class DoctorController:

    def find_by_national_id_controller(self, national_id):
        try:
            da = DoctorDa()
            da.find_by_national_id(national_id)
            return "فرد پیدا شد"

        except Exception as e:
            return e

    def save(self,name, family, national_id, date_birth, phone_number, username, password):
        try:
            # validation
            doctor = Doctor(name, family, national_id, date_birth, phone_number, username, password)
            da = DoctorDa()
            da.save(Doctor)
            return "فرد ثبت شد"
        except Exception as e:
            return e

    def remove_doctor_by_id_controller(id):
        try:
            da = DoctorDa()
            da.remove(id)
            return "فرد حذف شد"

        except Exception as e:
            return e

    def find_doctor_by_id_controller(id):
        try:
            da = DoctorDa()
            da.find_by_id(id)
            return "فرد پیدا شد"

        except Exception as e:
            return e

    def find_by_family_controller(family):
        try:
            da = DoctorDa()
            da.find_by_family(family)
            return "فرد پیدا شد"

        except Exception as e:
            return e

    def find_by_username_controller(username):
        try:
            da = DoctorDa()
            da.find_by_username(username)
            return "فرد پیدا شد"

        except Exception as e:
            return e

    def find_by_username_password_controller(username, password):
        try:
            da = DoctorDa()
            da.find_by_username_password(username, password)
            return "فرد مورد نظر پیدا شد"

        except Exception as e:
            return e

    class DoctorController:
        pass

