from son_quartier_en_chiffres import app
from flask import session, g, escape, redirect, url_for, render_template,\
                                request, Flask, Response, abort, jsonify
from pyproj import Proj, transform
from csv import reader, DictReader
from numpy import sqrt
import os


def distance_lambert(XY1, XY2):
    return sqrt((XY2[0] - XY1[0])**2 +  (XY2[1] - XY1[1])**2 )

def transform_wgs84_laea3135(lon, lat):
    wgs84 = Proj("+init=EPSG:4326")
    laea = Proj("+init=EPSG:3035")
    X, Y = transform(wgs84, laea, lon, lat)
    return X, Y

def exploit_db(file, x, y):
    base = DictReader(open(file,"rb"))
    data = []
    for row in base:
        x_base = float(row['x'])
        y_base = float(row['y'])
        if sqrt((x-x_base)**2 + (y-y_base)**2) < 300:
            data.append(row)
    print data
    return data


        #if (float(row[0]) - x)**2 < 100:
        #    print row




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/geoinformation/<latlng>')
def geoinformation(latlng):
        lat = float(latlng.split('(')[1].split(',')[0])
        lon = float(latlng.split('(')[1].split(',')[1].split(')')[0])
        x, y = transform_wgs84_laea3135(lon, lat)
        print lat, lon
        print x, y
        data = exploit_db('./son_quartier_en_chiffres/base.csv', x, y)
        return jsonify(data[0]['men_coll'])
