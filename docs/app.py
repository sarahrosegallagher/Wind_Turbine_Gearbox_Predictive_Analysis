from flask import Flask, render_template
from os.path import exists
from pathlib import Path
#from flask_sqlalchemy import SQLAlchemy
#from config import rds_password
import psycopg2 as psy
import get_data
import os

app = Flask(__name__)

# Use our RDS database to connect to data
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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reason_for_analysis.html")
def reason_for_analysis():
    return render_template('reason_for_analysis.html')

@app.route("/visualization.html")
def visualization():
    if (exists(working_directory / 'static\\json\\declare.json') == False):
        get_data.make_turbine_dataframes()
    return render_template('visualization.html')

@app.route("/tableau_visualizations.html")
def tableau_visualizations():
    return render_template('tableau_visualizations.html')

@app.route("/slideshow.html")
def slideshow():
    return render_template('slideshow.html')

@app.route("/supporting_links.html")
def supporting_links():
    return render_template('supporting_links.html')

if __name__ == '__main__':
    app.run()