from son_quartier_en_chiffres import app
from flask import session, g, escape, redirect, url_for, render_template,\
                                request, Flask, Response, abort, jsonify


@app.route('/')
def index():
    return render_template('app_test.html')


@app.route('/geoinformation/<latlng>')
def geoinformation(latlng):
        print(latlng)
        return jsonify(latlng)
