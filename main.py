from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import json
import pymysql
import pandas as pd
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super-secret-key'
with open('config.json','r') as c:
    params = json.load(c)["params"]

app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
app.secret_key = 'super-secret-key'
db = SQLAlchemy(app)

class Admin(db.Model):
    #==========Admin Table Data ====================
    t_username = db.Column(db.String(20), primary_key=True)
    t_password = db.Column(db.String(20), nullable=False)

class First_year(db.Model):
    #============first year table data ==================
    roll_no = db.Column(db.Integer, primary_key=True)
    st_name = db.Column(db.String(25), nullable=False)
    enrollment_no = db.Column(db.String(20), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    sub1 = db.Column(db.Integer, nullable=False)
    sub2 = db.Column(db.Integer, nullable=False)
    sub3 = db.Column(db.Integer, nullable=False)
    sub4 = db.Column(db.Integer, nullable=False)
    sub5 = db.Column(db.Integer, nullable=False)
    sub6 = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(30), nullable=False)

class Second_year(db.Model):
    #============second year table data ==================
    roll_no = db.Column(db.Integer, primary_key=True)
    st_name = db.Column(db.String(25), nullable=False)
    enrollment_no = db.Column(db.String(20), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    sub1 = db.Column(db.Integer, nullable=False)
    sub2 = db.Column(db.Integer, nullable=False)
    sub3 = db.Column(db.Integer, nullable=False)
    sub4 = db.Column(db.Integer, nullable=False)
    sub5 = db.Column(db.Integer, nullable=False)
    sub6 = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(30), nullable=False)

class Third_year(db.Model):
    #============third year table data ==================
    roll_no = db.Column(db.Integer, primary_key=True)
    st_name = db.Column(db.String(25), nullable=False)
    enrollment_no = db.Column(db.String(20), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    sub1 = db.Column(db.Integer, nullable=False)
    sub2 = db.Column(db.Integer, nullable=False)
    sub3 = db.Column(db.Integer, nullable=False)
    sub4 = db.Column(db.Integer, nullable=False)
    sub5 = db.Column(db.Integer, nullable=False)
    sub6 = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(30), nullable=False)

class Subject(db.Model):
    #============Subject table data ==================
    semester = db.Column(db.Integer, primary_key=True)
    sub1 = db.Column(db.String(50), nullable=False)
    sub2 = db.Column(db.String(50), nullable=False)
    sub3 = db.Column(db.String(50), nullable=False)
    sub4 = db.Column(db.String(50), nullable=False)
    sub5 = db.Column(db.String(50), nullable=False)
    sub6 = db.Column(db.String(50), nullable=False)
    

@app.route('/result', methods = ['GET','POST'])
def result():
    if(request.method == 'POST'):
        year = request.form.get('year')
        rollno = request.form.get('roll_no')

        def passing(result_st):
            st_total = result_st.sub1 + result_st.sub2 + result_st.sub3 + result_st.sub4 + result_st.sub5 + result_st.sub6
            if result_st.sub1 < 35 or result_st.sub2 < 35 or result_st.sub3 < 35 or result_st.sub4 < 35 or result_st.sub5 <35 or result_st.sub6 < 69:
                return "FAIL", "-", st_total
            else:
                st_grade = round((st_total*100)/700,2)
                st_grade = str(st_grade) + " %"
                return "PASS", st_grade, st_total

        if year == "Please choose Year" or rollno == '0':
            flash('Invalid Input')
            return redirect('/')
        elif year == "1st Year":
            result_st = First_year.query.filter_by(roll_no=rollno).first()
            if not result_st:
                flash(f'Roll no:- {rollno} Result has not published yet.')
                return redirect('/404')
            else:
                if result_st.semester == 1:
                    sub = Subject.query.filter_by(semester=1).first()
                    student_result , grade, total = passing(result_st)
                    return render_template('result.html', result = result_st, sub = sub, grade = grade, student_result = student_result, total = total)
                else:
                    sub = Subject.query.filter_by(semester=2).first()
                    student_result , grade, total = passing(result_st)
                    return render_template('result.html', result = result_st, sub = sub, grade = grade, student_result = student_result, total = total)
        
        elif year == "2nd Year":
            result_st = Second_year.query.filter_by(roll_no=rollno).first()
            if not result_st:
                flash(f'Roll no:- {rollno} Result has not published yet.')
                return redirect('/404')
            else:
                if result_st.semester == 3:
                    sub = Subject.query.filter_by(semester=3).first()
                    student_result , grade, total = passing(result_st)
                    return render_template('result.html', result = result_st, sub = sub, grade = grade, student_result = student_result, total = total)
                else:
                    sub = Subject.query.filter_by(semester=4).first()
                    student_result , grade, total = passing(result_st)
                    return render_template('result.html', result = result_st, sub = sub, grade = grade, student_result = student_result, total = total)
            
        elif year == "3rd Year":
            result_st = Third_year.query.filter_by(roll_no=rollno).first()
            if not result_st:
                flash(f'Roll no:- {rollno} Result has not published yet.')
                return redirect('/404')
            else:
                if result_st.semester == 5:
                    sub = Subject.query.filter_by(semester=5).first()
                    student_result , grade, total = passing(result_st)
                    return render_template('result.html', result = result_st, sub = sub, grade = grade, student_result = student_result, total = total)
                else:
                    sub = Subject.query.filter_by(semester=6).first()
                    return render_template('result.html', result = result_st, sub = sub)
    else:
        return render_template('index.html')

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if ('user' in session and session['user'] == params['username']):
        return render_template('dashboard.html')

    if request.method == 'POST':
        username = request.form.get('username')
        userpass = request.form.get('pass')
        admin = Admin.query.filter_by(t_username = username).first()
        if (username == admin.t_username and userpass == admin.t_password):
            session['user'] = username
            return render_template('dashboard.html')
    else:
        return render_template('login.html')

@app.route('/result-upload', methods=['GET','POST'])
def file_upload():
    if ('user' in session and session['user'] == params['username']):
        if request.method == 'POST':
            f = request.files['file']
            if f.filename == '':
                error = 'File not selected'
                return render_template('404.html', error = error)
            else:
                df = pd.read_csv(f)
                for i in range(df.shape[0]):
                    rollno = df.loc[i, "roll_no"]
                    rollno = int(rollno.item())
                    name = df.loc[i, "st_name"]
                    enroll = df.loc[i, "enrollment_no"]
                    semester = df.loc[i, "semester"]
                    semester = int(semester.item())
                    sub1 = df.loc[i, "sub1"]
                    sub1 = int(sub1.item())
                    sub2 = df.loc[i, "sub2"]
                    sub2 = int(sub2.item())
                    sub3 = df.loc[i, "sub3"]
                    sub3 = int(sub3.item())
                    sub4 = df.loc[i, "sub4"]
                    sub4 = int(sub4.item())
                    sub5 = df.loc[i, "sub5"]
                    sub5 = int(sub5.item())
                    sub6 = df.loc[i, "sub6"]
                    sub6 = int(sub6.item())

                    if semester == 1 or semester == 2:
                        entry = First_year(roll_no=rollno,st_name=name,enrollment_no=enroll,semester=semester,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6,date=datetime.now())
                    elif semester == 3 or semester == 4:
                        entry = Second_year(roll_no=rollno,st_name=name,enrollment_no=enroll,semester=semester,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6,date=datetime.now())
                    else:
                        entry = Third_year(roll_no=rollno,st_name=name,enrollment_no=enroll,semester=semester,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6,date=datetime.now())

                    db.session.add(entry)
                    db.session.commit()
                passing = "Data Updated Successfully"
                return render_template('dashboard.html', error = passing)
    else:
        return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/404')
def not_found():
    return render_template('404.html')

app.run(debug=True)