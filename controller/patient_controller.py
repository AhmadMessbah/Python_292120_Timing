from model.da.patient_da import PatientDa
from model.entity.patient import Patient
import tkinter.messagebox as msg


class PatientController:
    def save(self, name, family, national_id, date_birth, phone_number, username, password):
        try:
            patient = Patient(name, family, national_id, date_birth, phone_number, username, password)
            da = PatientDa()
            da.save(patient)
            return "فرد ثبت شد"
        except Exception as e:
            return e

    def remove(self, id):
        try:
            da = PatientDa()
            da.remove_by_id(Patient, id)
            return "فرد حذف شد"

        except Exception as e:
            return e

    def edit(self, id, name, family, national_id, date_birth, phone_number, username, password):

        try:
            da = PatientDa()
            patient = da.find_by_id(Patient, id)

            if patient:
                patient.name = name
                patient.family = family
                patient.national_id = national_id
                patient.date_birth = date_birth
                patient.phone_number = phone_number
                patient.username = username
                patient.password = password
                da.edit(patient)
                return "user edited"

        except Exception as e:
            return e

    def find_by_id(self, id):
        try:
            da = PatientDa()
            patient = da.find_by_id(Patient, id)
            print(patient)
            if patient:
                return f"find user with id {id}"
        except Exception as e:
            return e

    def find_by_family(self, family):
        try:
            da = PatientDa()
            patient = da.find_by_family(Patient, family)
            print(patient)
            if patient.family == family:
                return f"find user by {family}"

        except Exception as e:
            return e

    def find_by_national_id(self, national_id):
        try:
            da = PatientDa()
            patient = da.find_by_national_id(Patient, national_id)
            print(patient)
            if patient:
                return "فرد پیدا شد"

        except Exception as e:
            return e

    def find_by_username(self, username):
        try:
            da = PatientDa()
            da.find_by_username(username)
            return "فرد پیدا شد"

        except Exception as e:
            return e

    def find_by_username_password(self, username, password):
        try:
            da = PatientDa()
            da.find_by_username_password(username, password)
            return "فرد مورد نظر پیدا شد"

        except Exception as e:
            return e
