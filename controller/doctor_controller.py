from model.da.doctor_da import DoctorDa
from model.entity.doctor import Doctor
from model.tools.validation import *


class DoctorController:

    def save(self, name, family, national_id, date_birth, phone_number, username, password, skill):
        try:

            doctor = Doctor(
                #                 name_validator(name, "invalid name"),
                #                 name_validator(family, "invalid family"),
                #                 national_id_validator(national_id, "invalid national id"),
                #                 date_validator(date_birth, "invalid date"),
                #                 phone_number_validator(phone_number, "invalid phone number"),
                #                 username_validator(username, "invalid username"),
                #                 password_validator(password, "invalid password"),
                #                 name_validator(skil, "invalid skil")
                name, family, national_id, date_birth, phone_number, username, password, skill
            )
            da = DoctorDa()
            result = da.save(doctor)
            return result

        except Exception as e:
            # e.with_traceback()
            return e

    def remove(self, id):
        try:
            da = DoctorDa()
            result = da.remove_by_id(Doctor, id)
            return result
        except Exception as e:
            # e.with_traceback()
            print(e)

    def find_by_id(self, id):
        try:
            da = DoctorDa()
            result = da.find_by_id(Doctor, id)
            if result:
                print(result)
                return result

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

    def edit(self, id, name, family, national_id, date_birth, phone_number, username, password, skill):
        try:
            da = DoctorDa()
            doctor = da.find_by_id(Doctor, id)
            if doctor:
                doctor.name = name_validator(name, "invalid name")
                doctor.family = name_validator(family, "invalid family")
                doctor.national_id = national_id_validator(national_id, "invalid national id")
                doctor.date_birth = date_birth
                doctor.phone_number = phone_number_validator(phone_number, "invalid phone number")
                doctor.username = username_validator(username, "invalid username")
                doctor.password = password_validator(password, "invalid password")
                doctor.skill = name_validator(skill, "invalid skil")
                da.edit(doctor)
                return f"doctor {id} edited"
        except Exception as e:
            print(e)

    @classmethod
    def find_all(self):
        try:
            da = DoctorDa()
            doctors = da.find_all(Doctor)
            return doctors
        except Exception as e:
            print(e)
