import flask
from flask import Flask, render_template,g
import sqlite3
app = Flask(__name__)


 
@app.route('/')
@app.route('/jobs')

def jobs():
    return render_template('index.html')

PATH = "db/jobs.sqlite"

def open_connection():
    connection = getattr(g,'_database',None)
    if connection is None:
        connection,g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values=(), commit=False,single=False):
    connection = open_connection()
    cursor = connection.exectue(sql,values)
    if commit is True:
        results = connection.commit()
    # else:
    #     if single(cursotr.fetchone()) is True:
            
    cursor.close()
    return connection


's assurer que app_context est détruit quand close_connection est appelé'
@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g,'_connection',None)
    if connection is not None:
        connection.close()
    

