import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# 1. Set up the Database

# set up the engine
engine = create_engine ("sqlite:///hawaii.sqlite")

# reflect the database into classes
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# create variable for each class for reference
Measurement = Base.classes.measurement
Station = Base.classes.station

# create session link
session = Session(engine)

# 2. Set up Flask

# define Flask app
app = Flask(__name__)

# define the root route
@app.route("/")

# add the routing information
def welcome():
    return(
        '''
        Welcome to the Climate Analysis API! <br>
        Available Routes: <br>
        /api/v1.0/precipitation <br>
        /api/v1.0/stations <br>
        /api/v1.0/tobs <br>
        /api/v1.0/temp/start/end <br>
        ''')

# define the precipitation route
@app.route("/api/v1.0/precipitation")

# create the precipiration() function
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# define the stations route
@app.route("/api/v1.0/stations")

# define the stations() function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))  # np.ravel unravels the results into a one-dimensional array; next convert the unravelled results into a list using the list() function
    return jsonify(stations=stations)