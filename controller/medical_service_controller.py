from model.da.medical_service_da import MedicalServiceDa
from model.entity.medical_service import MedicalService
from model.tools.validation import name_validator
import tkinter.messagebox as msg


class MedicalServiceController:
    def save_medical_srvices_controller(self, title, description):
        try:
            if name_validator(title, "error"):
                service = MedicalService(title, description)
                da = MedicalServiceDa()
                da.save(service)
                return " ثبت شد"
        except Exception as e:
            msg.showerror("err", "error")

    def remove_medical_srvices_by_id_controller(self, id):
        try:
            da = MedicalServiceDa()
            da.remove(id)
            return " حذف شد"

        except Exception as e:
            return e

    def find_medical_srvices_by_title_controller(self, title):
        try:
            if name_validator(title, "error"):
                da = MedicalServiceDa()
                result = da.find_by_title(title)
                msg.showinfo("info", str(result))

                return "پیدا شد"

        except Exception as e:
            msg.showerror("err", "error")

    def edit(self,id,title,description):
        try:
            da = MedicalServiceDa()
            medical = da.find_by_id(MedicalService, id)

            if medical :
                medical.title = title
                medical.description = description
                da.edit(medical)

                msg.showinfo("info", str(medical))
        except Exception as e:
            # msg.showerror("err", e)
            e.with_traceback()

