from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import pymysql
import os
from datetime import datetime


@app.route('/')
def home():
    return render_template('index.html')


app.run(debug=True)