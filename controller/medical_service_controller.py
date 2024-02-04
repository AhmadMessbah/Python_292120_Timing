from model.da.medical_service_da import MedicalServiceDa
from model.entity.medical_service import MedicalService
from model.tools.validation import name_validator
import tkinter.messagebox as msg


class MedicalServiceController:
    def save(self, title, description):
        try:
            service = MedicalService(title, description)
            da = MedicalServiceDa()
            da.save(service)
            return f"medical service save {title}"
        except Exception as e:
            msg.showerror("err", "error")

    def remove(self, id):
        try:
            da = MedicalServiceDa()
            da.remove_by_id(MedicalService, id)
            return f"medical service {id} has been removed"

        except Exception as e:
            return e

    def find_by_title(self, title):
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

    def find_by_id(self, id):
        try:
            da = MedicalServiceDa()
            medical = da.find_by_id(MedicalService, id)
            print(medical)
            if medical:
                return f"find user with id {id}"
        except Exception as e:
            return e
