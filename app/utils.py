from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import joblib
import numpy as np

class Teacher(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(100), unique=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(10))
    high_school = db.Column(db.String(100))
    scholarship = db.Column(db.String(100))
    additional_work = db.Column(db.String(10))
    sports = db.Column(db.String(10))
    transport = db.Column(db.String(100))
    study_hours = db.Column(db.Float)
    attendance = db.Column(db.Float)
    reading = db.Column(db.Integer)
    notes = db.Column(db.Integer)
    listening = db.Column(db.Integer)
    project_work = db.Column(db.Integer)
    grade = db.Column(db.Float)

def predict_performance(student):
    model = joblib.load("models/performance_model.pkl")
    data = np.array([[student.age, student.study_hours, student.attendance,
                      student.reading, student.notes, student.listening,
                      student.project_work]]).reshape(1, -1)
    return model.predict(data)[0]