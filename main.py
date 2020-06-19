from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import pymysql
import os
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
    admin_name = db.Column(db.String(20), primary_key=True)
    pass_word = db.Column(db.String(20), nullable=False)

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
        
        error = "Result not declare yet"

        def passing(result_st):
            st_total = result_st.sub1 + result_st.sub2 + result_st.sub3 + result_st.sub4 + result_st.sub5 + result_st.sub6
            if result_st.sub1 < 35 or result_st.sub2 < 35 or result_st.sub3 < 35 or result_st.sub4 < 35 or result_st.sub5 <35 or result_st.sub6 < 69:
                return "FAIL", "-", st_total
            else:
                st_grade = round((st_total*100)/700,2)
                st_grade = str(st_grade) + " %"
                return "PASS", st_grade, st_total

        if year == "Please choose Year" or rollno == '0':
            return redirect('/')
        elif year == "1st Year":
            result_st = First_year.query.filter_by(roll_no=rollno).first()
            if not result_st:
                sub = Subject.query.filter_by(semester=0).first()
                return render_template('result.html', error = error, result = result_st, sub = sub)
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
                sub = Subject.query.filter_by(semester=0).first()
                return render_template('result.html', error = error, result = result_st, sub = sub)
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
                sub = Subject.query.filter_by(semester=0).first()
                return render_template('result.html', error = error, result = result_st, sub = sub)
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

@app.route('/dashboard')
def dashboard():
    return render_template('login.html')

@app.route('/')
def home():
    return render_template('index.html')

app.run(debug=True)