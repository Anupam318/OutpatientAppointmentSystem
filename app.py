from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Dummy data for doctors and appointments (for simplicity)
doctors = [
    {"id": 1, "name": "Dr. VIKRAM", "available_slots": 5},
    {"id": 2, "name": "Dr. RANDEEP", "available_slots": 3},
]

appointments = []

# Endpoint for listing doctors
@app.route('/doctors', methods=['GET'])
def get_doctors():
    return jsonify(doctors)

# Endpoint for booking appointments
@app.route('/appointments', methods=['POST'])
def book_appointment():
    data = request.get_json()
    doctor_id = data.get('doctor_id')

    # Check if the doctor exists
    doctor = next((d for d in doctors if d['id'] == doctor_id), None)
    if not doctor:
        return jsonify({"message": "Doctor not found"}), 404

    # Check if there are available slots
    if doctor['available_slots'] > 0:
        doctor['available_slots'] -= 1
        appointments.append({"doctor_id": doctor_id, "patient_name": data.get('patient_name')})
        return jsonify({"message": "Appointment booked successfully"})

    return jsonify({"message": "No available slots for this doctor"}), 400

# Endpoint for listing appointments
@app.route('/appointments', methods=['GET'])
def list_appointments():
    return jsonify(appointments)

if __name__ == '__main__':
    app.run(debug=True)
