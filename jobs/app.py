import flask
from flask import Flask, render_template,g
import sqlite3
app = Flask(__name__)

def open_connection:
    connection = getattr(g,'_database',None)
    return connection 
@app.route('/')
@app.route('/jobs')

def jobs():
    return render_template('index.html')

PATH = "db/jobs.sqlite"