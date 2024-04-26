from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin

import db

app = Flask(__name__)
app.secret_key = 'virtualSchool'  

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@app.route('/')
def index():
    students = db.get_all_students()
    return render_template('index.html', students=students)

@app.route('/filter', methods=['POST'])
def filter_students():
    if request.method == 'POST':
        data = request.json
        specialization = data['specialization']
        language = data['language']
        filtered_students = db.filter_students(specialization, language)
        return jsonify(filtered_students)

@app.route('/add_student')
@login_required
def add_student():
    return render_template('add_student.html')

@app.route('/submit_student', methods=['POST'])
@login_required
def submit_student():
    if request.method == 'POST':
        # Получаем данные из формы
        full_name = request.form['full_name']
        specialization = request.form['specialization']
        language_of_study = request.form['language_of_study']
        avg_professional_score = request.form['avg_professional_score']
        total_avg_score = request.form['total_avg_score']
        
        db.insert_student(full_name, specialization, language_of_study, avg_professional_score, total_avg_score)
        
        return redirect('/')
    else:
        return 'Method Not Allowed', 405

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'admin' and password == 'admin':
            user = User(username)
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error_message='Invalid username or password')
    else:
        return render_template('login.html')
    
@app.route('/edit_student', methods=['GET'])
def edit_student():
    student_id = request.args.get('student_id')
    student = db.get_student_by_id(student_id)
  
    return render_template('edit_student.html', student=student)

@app.route('/save_student', methods=['POST'])
def update_student_route():
    print('rab', flush=True)
    student_id = request.form['student_id']  
    full_name = request.form['full_name']
    specialization = request.form['specialization']
    language_of_study = request.form['language_of_study']
    avg_professional_score = request.form['avg_professional_score']
    total_avg_score = request.form['total_avg_score']
    db.update_student(student_id, full_name, specialization, language_of_study, avg_professional_score, total_avg_score)
    return redirect(url_for('edit_student', student_id=student_id))


@app.route('/delete_student', methods=['POST'])
def delete_student():
    student_id = request.json['student_id']
    db.delete_student(student_id)
    return jsonify({'success': True})

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
