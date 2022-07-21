from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import config import rds_password
# import visualizations

app = Flask(__name__)

# Use our RDS database to connect to data
app.config["MONGO_URI"] = f"postgresql://postgres:{rds_password}@wind-turbine-analysis.chv2nnusygyy.us-west-1.rds.amazonaws.com:5432/wind_turbine_analysis"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update_one({}, {"$set": mars_data}, upsert=True)
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run()