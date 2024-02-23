from flask import Flask, render_template, request
from controller.doctor_controller import DoctorController
from controller.medical_service_controller import MedicalServiceController
from controller.patient_controller import PatientController
from controller.timing_controller import TimingController
from controller.visit_controller import VisitController
from model.entity.patient import Patient

app = Flask(__name__, template_folder="view", static_folder="view/assets")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/medical", methods=['POST', "GET", "PUT", "DELETE"])
def medical():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        controller = MedicalServiceController()
        msg = controller.save(title, description)
    elif request.method == "PUT":
        id = request.form['id']
        title = request.form['title']
        description = request.form['description']
        controller = MedicalServiceController()
        msg = controller.edit(id, title, description)
    elif request.method == "DELETE":
        id = request.args.get('id')
        controller = MedicalServiceController()
        msg = controller.remove(id)
    return render_template("med_service.html", medical_list=MedicalServiceController.find_all())


@app.route("/medical/<id>")
def edit_medical(id):
    return render_template("medical_edit.html", medical=MedicalServiceController().find_by_id(id))


@app.route("/doctor", methods=["GET", 'POST', 'DELETE', "PUT"])
def doctor():
    if request.method == "POST":
        controller = DoctorController()
        name = request.form['name']
        family = request.form['family']
        national_id = request.form['national_id']
        date_birth = request.form['date_birth']
        phone_number = request.form['phone_number']
        username = request.form['username']
        password = request.form['password']
        skill = request.form['skill']
        msg = controller.save(name, family, national_id, date_birth, phone_number, username, password, skill)
        print(msg)
    elif request.method == "DELETE":
        id = request.args.get('id')
        controller = DoctorController()
        msg = controller.remove(id)
        print(msg)
    elif request.method == "PUT":
        id = request.form['id']
        name = request.form['name']
        family = request.form['family']
        national_id = request.form['national_id']
        date_birth = request.form['date_birth']
        phone_number = request.form['phone_number']
        username = request.form['username']
        password = request.form['password']
        skill = request.form['skill']
        controller = DoctorController()
        msg = controller.edit(id, name, family, national_id, date_birth, phone_number, username, password, skill)
        print(msg)
    return render_template("doctor.html", doctor_list=DoctorController.find_all())


@app.route("/doctor/<id>")
def edit_doctor(id):
    return render_template("doctor_edit.html", doctor=DoctorController().find_by_id(id))


@app.route("/patient", methods=["GET", 'POST', 'DELETE', "PUT"])
def patient():
    if request.method == "POST":
        name = request.form['name']
        family = request.form['family']
        national_id = request.form['national_id']
        date_birth = request.form['date_birth']
        phone_number = request.form['phone_number']
        username = request.form['username']
        password = request.form['password']
        controller = PatientController()
        msg = controller.save(name, family, national_id, date_birth, phone_number, username, password)
    elif request.method == "PUT":
        print("PUT", request.get_json())
        controller = PatientController()
        msg = controller.edit(**request.get_json(force=True))
    elif request.method == "DELETE":
        id = request.args.get('id')
        print("DELETE ID : ", id)
        controller = PatientController()
        controller.remove(id)
    return render_template("patient.html", patient_list=PatientController.find_all())


@app.route("/patient/<id>")
def edit_patient(id):
    return render_template("patient_edit.html", patient=PatientController().find_by_id(id))


@app.route("/visit", methods=["GET", 'POST', 'DELETE', "PUT"])
def visit():
    if request.method == "POST":
        doctor = request.form.get("doctor_id")
        doctor_in_timing = TimingController().find_by_doctor_id(doctor)
        print(str(doctor))
        timing = request.form['timing_id']
        visit_time = request.form['visit_time']
        duration = request.form['duration']
        payment = request.form['payment']
        controller = VisitController()
        msg = controller.save(patient, timing, visit_time, duration, payment)
        return msg
    elif request.method == "DELETE":
        id = request.args.get('id')
        controller = VisitController()
        msg = controller.remove(id)
        return msg
    elif request.method == "PUT":
        id = request.form['id']
        visit_time = request.form['visit_time']
        duration = request.form['duration']
        payment = request.form['payment']
        controller = VisitController()
        msg = controller.edit(id, visit_time, duration, payment)
        return msg
    return render_template("visit.html", visit_list=VisitController.find_all(),
                           doctor_list=DoctorController.find_all() )


@app.route("/visit/<id>")
def edit_visit(id):
    return render_template("visit_edit.html", visit=VisitController().find_by_id(id))


@app.route("/timing", methods=["GET", "POST", "PUT", "DELETE"])
def timimng():
    if request.method == 'POST':
        doctor = request.form.get('doctor')
        print(str(doctor))
        doctor_list = DoctorController().find_by_id(doctor)
        timing_date = request.form['timing_date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        controller = TimingController()
        msg = controller.save(doctor_list, timing_date, start_time, end_time)
    elif request.method == 'PUT':
        id = request.form['id']
        timing_date = request.form['timing_date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        controller = TimingController()
        msg = controller.edit(id, timing_date, start_time, end_time)
        return msg
    elif request.method == 'DELETE':
        id = request.args.get('id')
        controller = TimingController()
        msg = controller.remove(id)
        return msg
    return render_template("timing.html", timing_list=TimingController.find_all(),
                           doctor_list=DoctorController.find_all())


@app.route("/timing/<id>")
def edit_timing(id):
    return render_template("timing_edit.html", timing=TimingController().find_by_id(id))


if __name__ == "__main__":
    app.run(debug=True)
