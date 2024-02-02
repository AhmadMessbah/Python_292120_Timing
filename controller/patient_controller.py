from model.da.patient_da import PatientDa
from model.entity.patient import Patient


class PatientController:
    def save_patient_controller(self, name, family, national_id, date_birth, phone_number, username, password):
        try:
            patient = Patient(name, family, national_id, date_birth, phone_number, username, password)
            da = PatientDa()
            da.save(patient)
            return "فرد ثبت شد"
        except Exception as e:
            return e

    def remove_patient_by_id_controller(self, id):
        try:
            da = PatientDa()
            da.remove(id)
            return "فرد حذف شد"

        except Exception as e:
            return e

    def find_patient_by_id_controller(self, id):
        try:
            da = PatientDa()
            da.find_by_id(id)
            return "فرد پیدا شد"

        except Exception as e:
            return e

    def find_by_family_controller(self, family):
        try:
            da = PatientDa()
            da.find_by_family(family)
            return "فرد پیدا شد"

        except Exception as e:
            return e

    def find_by_national_id_controller(self, national_id):
        try:
            da = PatientDa()
            da.find_by_national_id(national_id)
            return "فرد پیدا شد"

        except Exception as e:
            return e

    def find_by_username_controller(self, username):
        try:
            da = PatientDa()
            da.find_by_username(username)
            return "فرد پیدا شد"

        except Exception as e:
            return e

    def find_by_username_password_controller(self,username,password):
        try:
            da = PatientDa()
            da.find_by_username_password(username,password)
            return "فرد مورد نظر پیدا شد"

        except Exception as e:
            return e

