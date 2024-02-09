from flask import Flask, render_template, request
from controller.doctor_controller import DoctorController
from controller.medical_service_controller import MedicalServiceController
from controller.patient_controller import PatientController
from controller.timing_controller import TimingController
from controller.visit_controller import VisitController

app = Flask(__name__, template_folder="view", static_folder="view/assets")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/medical", methods=['POST',"GET"])
def medical():
    if request.method == "GET":
        return render_template("med_service.html")
    elif request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        controller = MedicalServiceController()
        msg = controller.save(title, description)
        return msg


@app.route("/doctor", methods=["GET", 'POST', 'DELETE', "PUT"])
def doctor():
    if request.method == "GET":
        return render_template("doctor.html")
    elif request.method == "POST":
        name = request.form['name']
        family = request.form['family']
        national_id = request.form['national_id']
        date_birth = request.form['date_birth']
        phone_number = request.form['phone_number']
        username = request.form['username']
        password = request.form['password']
        skil = request.form['skil']
        medical_service = request.form['medical_service']

        controller = DoctorController()
        msg = controller.save(name, family, national_id, date_birth, phone_number, username, password, skil,
                              medical_service)
        return msg
    elif request.method == "DELETE":
        id = request.form['id']
        controller = DoctorController()
        msg = controller.remove_doctor_by_id(id)
        return msg


@app.route("/patient", methods=["GET",'POST', 'DELETE', "PUT"])
def patient():
    if request.method == 'GET':
        return render_template("patient.html")
    elif request.method == "POST":
        name = request.form['name']
        family = request.form['family']
        national_id = request.form['national_id']
        date_birth = request.form['date_birth']
        phone_number = request.form['phone_number']
        username = request.form['username']
        password = request.form['password']
        controller = PatientController()
        msg = controller.save(name, family, national_id, date_birth, phone_number, username, password)
        return msg
    elif request.method == "PUT":
        id = request.form['id']
        name = request.form['name']
        family = request.form['family']
        national_id = request.form['national_id']
        date_birth = request.form['date_birth']
        phone_number = request.form['phone_number']
        username = request.form['username']
        password = request.form['password']
        controller = PatientController()
        msg = controller.edit(id, name, family, national_id, date_birth, phone_number, username, password)
        return msg
    elif request.method == "DELETE":
        id = request.form['id']
        controller = PatientController()
        msg = controller.remove(id)
        return msg


@app.route("/visit", methods=["GET",'POST', 'DELETE', "PUT"])
def visit():
    if request.method == "GET":
        return render_template("visit.html")
    elif request.method == "POST":
        patient_id = request.form['patient_id']
        timing_id = request.form['timing_id']
        visit_time = request.form['visit_time']
        duration = request.form['duration']
        payment = request.form['payment']
        controller = VisitController()
        msg = controller.save(patient_id, timing_id, visit_time, duration, payment)
        return msg
    elif request.method == "DELETE":
        id = request.form['id']
        controller = VisitController()
        msg = controller.remove(id)
        return msg
    elif request.method == "PUT":
        id = request.form['id']
        patient_id = request.form['patient_id']
        timing_id = request.form['timing_id']
        visit_time = request.form['visit_time']
        duration = request.form['duration']
        payment = request.form['payment']
        controller = VisitController()
        msg = controller.edit(id, patient_id, timing_id, visit_time, duration, payment)
        return msg


@app.route("/timing", methods=["GET",'POST'])
def timimng():
    if request.method == 'GET':
        return render_template("timing.html")
    elif request.method == 'POST':
        doctor = request.form['doctor']
        timing_date = request.form['timing_id']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        controller = TimingController()
        msg = controller.save(doctor, timing_date, start_time, end_time)
        return msg


app.run(port=80)
