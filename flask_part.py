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
def precipitation(start_date):
    data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >=func.strtime("%Y-%m-%d", start_date).order_by(Measurement.date).all()  
    result_list =[]
    for d in data:
        prcp_dict = {}
        prcp_dict['date'] = d.prcp
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
def tobs(start_date):
    data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= func.strtime("%Y-%m-%d", start_date).order_by(Measurement.date)).all()
    result_list = []
    for d in data:
        tobs_dict = {}
        tobs_dict['date'] = d.date
        tobs_dict['tobs'] = d.tobs
        result_list.append(tobs_dict)

    return jsonify(result_list)

@app.route("/api/v1.0/<start_date>)
def start_date(start_date):
    starts_date_dict = {}
    data = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= func.strtime("%Y-%m-%d", start_date).order_by(Measurement.date)).all()
    data_list = list(np.ravel(data))
    starts_date_dict["t-max"] = data_list[1]
    starts_date_dict["t-min"] = data_list[0]
    starts_date_dict["t-avg"] = data_list[2]
    return jsonify(starts_date_dict)

@app.route("/api/v1.0/<start_date>/<end_date>)
def start_end_dates(start_date, end_date):
    start_end_dates_dict = {}
    data = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= func.strtime("%Y-%m-%d", start_date).filter(Measurement.date <= func.strtime("%Y-%m-%d", end_date).all()
    data_list = list(np.ravel(data))
    start_end_dates_dict["t-max"] = data_list[1]
    start_end_dates_dict["t-min"] = data_list[0]
    start_end_dates_dict["t-avg"] = data_list[2]
    return jsonify(sstart_end_dates_dict)

if __name__ == "__main__":
    app.run(debug=True)