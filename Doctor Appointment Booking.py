from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# Doctor database with different locations in Chennai
doctors = [
    {"name": "Dr. John Smith", "specialization": "General Medicine", "address": "Anna Nagar, Chennai", "contact": "+91-9876543210", "locality": "Anna Nagar", "available_days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "consultation_fee": 500.00},
    {"name": "Dr. Sarah Johnson", "specialization": "General Medicine", "address": "T Nagar, Chennai", "contact": "+91-9876543211", "locality": "T Nagar", "available_days": ["Monday", "Wednesday", "Friday"], "consultation_fee": 600.00},
    {"name": "Dr. Rajesh Kumar", "specialization": "Cardiology", "address": "Adyar, Chennai", "contact": "+91-9876543212", "locality": "Adyar", "available_days": ["Tuesday", "Thursday", "Saturday"], "consultation_fee": 1000.00},
    {"name": "Dr. Priya Raman", "specialization": "Cardiology", "address": "Velachery, Chennai", "contact": "+91-9876543213", "locality": "Velachery", "available_days": ["Monday", "Wednesday", "Friday"], "consultation_fee": 1200.00},
    {"name": "Dr. Arun Kumar", "specialization": "Psychiatry", "address": "Mylapore, Chennai", "contact": "+91-9876543214", "locality": "Mylapore", "available_days": ["Monday", "Tuesday", "Thursday"], "consultation_fee": 800.00},
    {"name": "Dr. Maya Krishnan", "specialization": "Psychiatry", "address": "Tambaram, Chennai", "contact": "+91-9876543215", "locality": "Tambaram", "available_days": ["Wednesday", "Friday", "Saturday"], "consultation_fee": 900.00},
    {"name": "Dr. Vikram Singh", "specialization": "Clinical Psychology", "address": "Porur, Chennai", "contact": "+91-9876543216", "locality": "Porur", "available_days": ["Monday", "Wednesday", "Friday"], "consultation_fee": 700.00},
    {"name": "Dr. Anjali Desai", "specialization": "Clinical Psychology", "address": "Guindy, Chennai", "contact": "+91-9876543217", "locality": "Guindy", "available_days": ["Tuesday", "Thursday", "Saturday"], "consultation_fee": 750.00},
    {"name": "Dr. Karthik Raja", "specialization": "Neurology", "address": "Chromepet, Chennai", "contact": "+91-9876543218", "locality": "Chromepet", "available_days": ["Monday", "Tuesday", "Friday"], "consultation_fee": 1100.00},
    {"name": "Dr. Lakshmi Menon", "specialization": "Neurology", "address": "KK Nagar, Chennai", "contact": "+91-9876543219", "locality": "KK Nagar", "available_days": ["Wednesday", "Thursday", "Saturday"], "consultation_fee": 1150.00},
    {"name": "Dr. Ramesh Iyer", "specialization": "Pediatrics", "address": "Nungambakkam, Chennai", "contact": "+91-9876543220", "locality": "Nungambakkam", "available_days": ["Monday", "Wednesday", "Friday"], "consultation_fee": 600.00},
    {"name": "Dr. Shalini Gupta", "specialization": "Pediatrics", "address": "Pallavaram, Chennai", "contact": "+91-9876543221", "locality": "Pallavaram", "available_days": ["Tuesday", "Thursday", "Saturday"], "consultation_fee": 650.00}
]

appointments = []

@app.route('/')
def index():
    return render_template('appointment.html')

@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    appointment = {
        'patient_name': request.form['patient_name'],
        'patient_age': request.form['patient_age'],
        'patient_location': request.form['patient_location'],
        'patient_email': request.form['patient_email'],
        'patient_contact': request.form['patient_contact'],
        'symptoms': request.form['symptoms'],
        'diagnosis': request.form['diagnosis'],
        'doctor_specialization': request.form['doctor_specialization']
    }
    appointments.append(appointment)
    return redirect(url_for('doctors_page', location=appointment['patient_location']))

@app.route('/doctors')
def doctors_page():
    patient_location = request.args.get('location', '')
    # In a real application, you would implement proper location-based filtering
    return render_template('doctors.html', doctors=doctors)

if __name__ == '__main__':
    app.run(port=5004, debug=True)