from flask import Flask, render_template, request
from controller.doctor_controller import DoctorController
from controller.medical_service_controller import MedicalServiceController
from controller.patient_controller import PatientController
from controller.visit_controller import VisitController

app = Flask(__name__)

app.route("/")


def home():
    return render_template("")


app.route("/medical", methods=['POST'])


def medical():
    title = request.form['title']
    description = request.form['description']
    controller = MedicalServiceController()
    msg = controller.save(title, description)
    return msg


app.route("/doctor", methods=['POST'])


def doctor():
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


app.route("/patient", methods=['POST'])


def patient():
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


app.route("/visit", methods=['POST'])


def visit():
    patient_id = request.form['patient_id']
    timing_id = request.form['timing_id']
    visit_time = request.form['visit_time']
    duration = request.form['duration']
    payment = request.form['payment']
    controller = VisitController()
    msg = controller.save(patient_id, timing_id, visit_time, duration, payment)
    return msg


app.run(port=80)
