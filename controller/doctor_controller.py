from model.da.doctor_da import DoctorDa
from model.entity.doctor import Doctor
from model.tools.validation import *


class DoctorController:

    def save(self, name, family, national_id, date_birth, phone_number, username, password, skil, medical_service):
        try:

            doctor = Doctor(name_validator(name, "invalid name"),
                            name_validator(family, "invalid family"),
                            national_id_validator(national_id, "invalid national id"),
                            date_validator(date_birth, "invalid date"),
                            phone_number_validator(phone_number, "invalid phone number"),
                            username_validator(username, "invalid username"),
                            password_validator(password, "invalid password"),
                            name_validator(skil, "invalid skil"),
                            medical_service
                            )
            da = DoctorDa()
            result = da.save(doctor)
            if result:
                return f"{doctor} saved successfully"

        except Exception as e:
            return e

    def remove_doctor_by_id(id):
        try:
            da = DoctorDa()
            result = da.remove(id)
            if result:
                return f"remove doctor by id {id}"

        except Exception as e:
            return e

    def find_doctor_by_id(id):
        try:
            da = DoctorDa()
            result = da.find_by_id(Doctor, id)
            if result:
                return f"find doctor by id: {id}"

        except Exception as e:
            return e

    def find_by_family(family):
        try:
            da = DoctorDa()
            result = da.find_by_family(family)
            if result:
                return f"find doctor by family{family}"

        except Exception as e:
            return e

    def find_by_username(username):
        try:
            da = DoctorDa()
            result = da.find_by_username(username)
            if result:
                return f"find doctor by username {username}"

        except Exception as e:
            return e

    def find_by_username_password(username, password):
        try:
            da = DoctorDa()
            result = da.find_by_username_password(username, password)
            if result:
                return f"find doctor by username {username}"

        except Exception as e:
            return e

    def find_by_national_id(national_id):
        try:
            if national_id_validator(national_id, "invalid nationalId"):
                da = DoctorDa()
                result = da.find_by_national_id(national_id)
                if result:
                    return f"find doctor by nationalId : {national_id}"

        except Exception as e:
            return e
