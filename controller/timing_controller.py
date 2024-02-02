from model.da.timing_da import TimingDa
from model.entity.timing import Timing
from model.tools.validation import date_validator,time_validator
import tkinter.messagebox as msg
class TimingController:
    def save(self, date, start_time, end_time, status=True):
        try:
            if date_validator(date, "error") and time_validator(start_time, "error") and time_validator(end_time, "error"):
                timing = Timing(date, start_time,end_time)
                da = TimingDa()
                da.save(timing)
                return " ثبت شد"
        except Exception as e:
            msg.showerror("error",f"error : {e}")

    def edit(self, date, start_time, end_time, status):
        pass

    def remove(self, id):
        pass


    def find_all(self):
        pass


    def find_by_date(self, date):
       pass


    def find_by_start_time(self, start_time):
        pass

    def find_by_end_time(self, end_time):
        pass

    def find_by_doctor_id(self, doctor_id):
        pass