# 1. import dependencies
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Database Setup 

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def welcome():
    return 
    f"Welcome to Climate Analysus and Exploration! <br/> "
    f"Available Router: <br/>"
    f"/api/v1.0/precipitation"
    f"/api/v1.0/stations"
    f"/api/v1.0/tobs"
    f"/api/v1.0/<start>"
    f"/api/v1.0/<start>/<end>"

# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precipitation():
    data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >'2016-08-23').order_by(Measurement.date).all()  
    result_list =[]
    for d in data:
        prcp_dict = {}
        prcp_dict['date'] = d.prcp
        prcp_dict['prcp'] = d.prcp
        result_list.append(prcp_dict)
    return jsonify(result_list)

@app.route("/api/v1.0/stations")
def stations():
    data = session.query(Station.station, Station.name).all()
    result_list = []
    for d in data:
        station_dict = {}
        station_dict['station'] = d.station
        station_dict['name'] = d.name
        result_list.append(station_dict)
    return jsonify(result_list)

@app.route("/api/v1.0/tobs")
def tobs():
    data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >'2016-08-23').all()
    result_list = []
    for d in data:
        tobs_dict = {}
        tobs_dict['date'] = result.date
        tobs_dict['tobs'] = result.tobs
        result_list.append(tobs_dict)

    return jsonify(result_list)


if __name__ == "__main__":
    app.run(debug=True)