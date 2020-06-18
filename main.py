from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import pymysql
import os
from datetime import datetime

app = Flask(__name__)

with open('config.json','r') as c:
    params = json.load(c)["params"]

app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
app.secret_key = 'super-secret-key'

db = SQLAlchemy(app)


@app.route('/')
def home():
    #return "hello"
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

app.run(debug=True)