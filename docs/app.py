<<<<<<< HEAD
from flask import Flask, render_template, redirect, url_for
import os
import json
#from flask_sqlalchemy import SQLAlchemy
from config import rds_password
import psycopg2 as psy
import get_data
=======
from flask import Flask, render_template
from os.path import exists
from pathlib import Path
#from flask_sqlalchemy import SQLAlchemy
#from config import rds_password
import psycopg2 as psy
import get_data
import os
>>>>>>> cleanest

app = Flask(__name__)

# Use our RDS database to connect to data
<<<<<<< HEAD
def get_db_connection():
    conn = psy.connect(dbname="wind_turbine_analysis", 
                        user="postgres", 
                        password=rds_password, 
                        host="wind-turbine-analysis.chv2nnusygyy.us-west-1.rds.amazonaws.com"
                        )
    return conn

#app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:{rds_password}@wind-turbine-analysis.chv2nnusygyy.us-west-1.rds.amazonaws.com:5432/wind_turbine_analysis"
=======
#def get_db_connection():
#    conn = psy.connect(dbname="wind_turbine_analysis", 
#                        user="postgres", 
#                        password=rds_password, 
#                        host="wind-turbine-analysis.chv2nnusygyy.us-west-1.rds.amazonaws.com"
 #                       )
#    return conn

#pathing solution using pathlib's Path object
working_directory = Path(__file__).absolute().parent

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:password@wind-turbine-analysis.chv2nnusygyy.us-west-1.rds.amazonaws.com:5432/wind_turbine_analysis"
>>>>>>> cleanest

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reason_for_analysis.html")
def reason_for_analysis():
    return render_template('reason_for_analysis.html')

@app.route("/visualization.html")
def visualization():
<<<<<<< HEAD
    get_data.make_turbine_dataframes()
=======
    if (exists(working_directory / 'static\\json\\declare.json') == False):
        get_data.make_turbine_dataframes()
>>>>>>> cleanest
    return render_template('visualization.html')

@app.route("/fourth.html")
def fourth():
    return render_template('fourth.html')

@app.route("/fifth.html")
def fifth():
    return render_template('fifth.html')

@app.route("/sixth.html")
def sixth():
    return render_template('sixth.html')

if __name__ == '__main__':
    app.run()