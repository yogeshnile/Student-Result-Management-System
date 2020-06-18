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
    sub1 = db.Column(db.Integer, nullable=False)
    sub2 = db.Column(db.Integer, nullable=False)
    sub3 = db.Column(db.Integer, nullable=False)
    sub4 = db.Column(db.Integer, nullable=False)
    sub5 = db.Column(db.Integer, nullable=False)
    sub6 = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(30), nullable=False)

class Second_year(db.Model):
    #============second year table data ==================
    roll_no = db.Column(db.Integer, primary_key=True)
    st_name = db.Column(db.String(25), nullable=False)
    enrollment_no = db.Column(db.String(20), nullable=False)
    sub1 = db.Column(db.Integer, nullable=False)
    sub2 = db.Column(db.Integer, nullable=False)
    sub3 = db.Column(db.Integer, nullable=False)
    sub4 = db.Column(db.Integer, nullable=False)
    sub5 = db.Column(db.Integer, nullable=False)
    sub6 = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(30), nullable=False)

class Third_year(db.Model):
    #============third year table data ==================
    roll_no = db.Column(db.Integer, primary_key=True)
    st_name = db.Column(db.String(25), nullable=False)
    enrollment_no = db.Column(db.String(20), nullable=False)
    sub1 = db.Column(db.Integer, nullable=False)
    sub2 = db.Column(db.Integer, nullable=False)
    sub3 = db.Column(db.Integer, nullable=False)
    sub4 = db.Column(db.Integer, nullable=False)
    sub5 = db.Column(db.Integer, nullable=False)
    sub6 = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(30), nullable=False)

@app.route('/result', methods = ['GET','POST'])
def result():
    if(request.method == 'POST'):
        year = request.form.get('year')
        rollno = request.form.get('roll_no')
        
        error = "Result not declare yet"

        if year == "Please choose Year":
            return redirect('/')
        elif year == "1st Year":
            result_st = First_year.query.filter_by(roll_no=rollno).first()
            if not result_st:
                return render_template('result.html', error = error, result = result_st)
            else:
                return render_template('result.html', result = result_st)
        
        elif year == "2nd Year":
            result_st = Second_year.query.filter_by(roll_no=rollno).first()
            if not result_st:
                return render_template('result.html', error = error, result = result_st)
            else:
                return render_template('result.html', result = result_st)
            
        elif year == "3rd Year":
            result_st = Third_year.query.filter_by(roll_no=rollno).first()
            if not result_st:
                return render_template('result.html', error = error, result = result_st)
            else:
                return render_template('result.html', result = result_st)

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('login.html')

@app.route('/')
def home():
    return render_template('index.html')

app.run(debug=True)