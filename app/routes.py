from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .utils import Teacher, Student, db, login_manager, predict_performance

main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return Teacher.query.get(int(user_id))

@main.route('/')
def home():
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        teacher = Teacher.query.filter_by(username=request.form['username']).first()
        if teacher and teacher.check_password(request.form['password']):
            login_user(teacher)
            return redirect(url_for('main.dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/dashboard')
@login_required
def dashboard():
    students = Student.query.all()
    return render_template('dashboard.html', students=students)

@main.route('/add-student', methods=['GET', 'POST'])
@login_required
def add_student():
    if request.method == 'POST':
        student = Student(
            student_id=request.form['student_id'],
            age=int(request.form['age']),
            sex=request.form['sex'],
            high_school=request.form['high_school'],
            scholarship=request.form['scholarship'],
            additional_work=request.form['additional_work'],
            sports=request.form['sports'],
            transport=request.form['transport'],
            study_hours=float(request.form['study_hours']),
            attendance=float(request.form['attendance']),
            reading=int(request.form['reading']),
            notes=int(request.form['notes']),
            listening=int(request.form['listening']),
            project_work=int(request.form['project_work'])
        )
        student.grade = predict_performance(student)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('add_student.html')