from model.da.timing_da import TimingDa
from model.entity.timing import Timing
from model.tools.validation import *
import tkinter.messagebox as msg


class TimingController:
    def save(self, doctor, date, start_time, end_time):
        try:

            timing = Timing(date, start_time, end_time, doctor)
            da = TimingDa()
            result = da.save(timing)
            if result:
                print(result)
        except Exception as e:
            print(e)

    def edit(self, id, date, start_time, end_time):
        try:
            da = TimingDa()
            timing = da.find_by_id(Timing, id)

            if timing:
                timing.date = date
                timing.start_time = start_time
                timing.end_time = end_time
                result = da.edit(timing)
                print(result)

        except Exception as e:
            print(e)

    def remove(self, id):
        try:
            da = TimingDa()
            da.remove_by_id(Timing, id)
            return f"medical service {id} has been removed"

        except Exception as e:
            print(e)

    def find_by_id(self, id):
        try:
            da = TimingDa()
            time = da.find_by_id(Timing, id)
            print(time)
            if time:
                return f"find time with id : {id}"
        except Exception as e:
            print(e)

    @classmethod
    def find_all(cls):
        try:
            da = TimingDa()
            timing = da.find_all(Timing)
            return timing
        except Exception as e:
            return e

    def find_by_date(self, date):
        try:
            if date_validator(date, "error"):
                da = TimingDa()
                result = da.find_by_date(date)
                msg.showinfo("info", str(result))

                return "found"

        except Exception as e:
            msg.showerror("error", f"error : {e}")

    def find_by_start_time(self, start_time):
        try:
            if date_validator(start_time, "error"):
                da = TimingDa()
                result = da.find_by_start_time(start_time)
                msg.showinfo("info", str(result))

                return "found"

        except Exception as e:
            msg.showerror("error", f"error : {e}")

    def find_by_end_time(self, end_time):
        try:
            if date_validator(end_time, "error"):
                da = TimingDa()
                result = da.find_by_end_time(end_time)
                msg.showinfo("info", str(result))

                return "found"

        except Exception as e:
            msg.showerror("error", f"error : {e}")

    def find_by_doctor_id(self, doctor_id):
        try:

            da = TimingDa()
            result = da.find_by_doctor_id(doctor_id)
            return result

        except Exception as e:
            msg.showerror("error", f"error : {e}")
