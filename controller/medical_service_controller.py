from model.da.medical_service_da import MedicalServiceDa
from model.entity.medical_service import MedicalService
from model.tools.validation import name_validator
from model.tools.validation import *
import tkinter.messagebox as msg


class MedicalServiceController:
    def save(self, title, description):
        try:
            service = MedicalService(title, description)
            da = MedicalServiceDa()
            da.save(service)
            return service
        except Exception as e:
            print(e)

    def remove(self, id):
        try:
            da = MedicalServiceDa()
            result = da.find_by_id(MedicalService, id)
            if result:
                da.remove_by_id(MedicalService, id)
                return result

        except Exception as e:
            print(e)

    def find_by_title(self, title):
        try:
            if name_validator(title, "invalid title"):
                da = MedicalServiceDa()
                result = da.find_by_title(title)
                if result:
                    return result
        except Exception as e:
            print(e)

    def edit(self, id, title, description):
        try:
            da = MedicalServiceDa()
            medical = da.find_by_id(MedicalService, id)

            if medical:
                medical.title = title
                medical.description = description
                result = da.edit(medical)
                return result
        except Exception as e:
            print(e)

    def find_by_id(self, id):
        try:
            da = MedicalServiceDa()
            medical = da.find_by_id(MedicalService, id)
            print(medical)
            if medical:
                return medical
        except Exception as e:
            print(e)
    @classmethod
    def find_all(self):
        try:
            da = MedicalServiceDa()
            medical = da.find_all(MedicalService)
            print(medical)
            return medical


        except Exception as e:
            print(e)
