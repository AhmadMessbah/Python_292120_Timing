from model.da.patient_da import PatientDa
from model.entity.patient import Patient
from model.tools.validation import *


class PatientController:
    def save(self, name, family, national_id, date_birth, phone_number, username, password):
        try:
            patient = Patient(name_validator(name, "invalid name"),
                              name_validator(family, "invalid family"),
                              national_id_validator(national_id, "invalid nationalId"),
                              date_validator(date_birth, "invalid date_birth"),
                              phone_number_validator(phone_number, "invalid phone number"),
                              username_validator(username, "invalid username"),
                              password_validator(password, "invalid password")
                              )
            da = PatientDa()
            da.save(patient)
            return "فرد ثبت شد"
        except Exception as e:
            print(e)

    def remove(self, id):
        try:
            da = PatientDa()
            da.remove_by_id(Patient, id)
            return "فرد حذف شد"

        except Exception as e:
            print(e)

    def edit(self, id, name, family, national_id, date_birth, phone_number, username, password):

        try:
            da = PatientDa()
            patient = da.find_by_id(Patient, id)

            if patient:
                patient.name = name_validator(name, "invalid name")
                patient.family = name_validator(family, "invalid family")
                patient.national_id = national_id_validator(national_id, "invalid nationalId")
                patient.date_birth = date_validator(date_birth, "invalid date_birth")
                patient.phone_number = phone_number_validator(phone_number, "invalid phone number")
                patient.username = username_validator(username, "invalid username")
                patient.password = password_validator(password, "invalid password")
                da.edit(patient)
                return "user edited"

        except Exception as e:
            print(e)

    def find_by_id(self, id):
        try:
            da = PatientDa()
            patient = da.find_by_id(Patient, id)
            print(patient)
            if patient:
                return f"find user with id {id}"
        except Exception as e:
            print(e)

    def find_by_family(self, family):
        try:
            da = PatientDa()
            patient = da.find_by_family(family)
            print(patient)
            # Patient.family == family
            if patient:
                return f"find user by {family}"

        except Exception as e:
            print(e)

    def find_by_national_id(self, national_id):
        try:
            da = PatientDa()
            patient = da.find_by_national_id(national_id)
            print(patient)
            if patient:
                return "فرد پیدا شد"

        except Exception as e:
            print(e)

    def find_by_username(self, username):
        try:
            da = PatientDa()
            da.find_by_username(username)
            return "فرد پیدا شد"

        except Exception as e:
            print(e)

    def find_by_username_password(self, username, password):
        try:
            da = PatientDa()
            da.find_by_username_password(username, password)
            return "فرد مورد نظر پیدا شد"

        except Exception as e:
            print(e)
