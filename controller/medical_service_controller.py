from model.da.medical_service_da import MedicalServiceDa
from model.entity.medical_service import MedicalService


class MedicalServiceController:
    def save_medical_srvices_controller(self, title, description):
        try:
            service = MedicalService(title, description)
            da = MedicalServiceDa()
            da.save(service)
            return " ثبت شد"
        except Exception as e:
            return e

    def remove_medical_srvices_by_id_controller(self, id):
        try:
            da = MedicalServiceDa()
            da.remove(id)
            return " حذف شد"

        except Exception as e:
            return e

    def find_medical_srvices_by_title_controller(self, title):
        try:
            da = MedicalServiceDa()
            da.find_by_title(title)
            return "پیدا شد"

        except Exception as e:
            return e
