from flask import Flask, render_template, redirect, url_for
#from flask_sqlalchemy import SQLAlchemy
from config import rds_password
# import visualizations

app = Flask(__name__)

# Use our RDS database to connect to data
#app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:{rds_password}@wind-turbine-analysis.chv2nnusygyy.us-west-1.rds.amazonaws.com:5432/wind_turbine_analysis"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reason_for_analysis.html")
def reason_for_analysis():
    return render_template('reason_for_analysis.html')

@app.route("/third.html")
def third():
    return render_template('third.html')

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