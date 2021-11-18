#!/usr/bin/env python3

import os
import sys
import json
import threading
import time
from flask import Flask, render_template, jsonify, request
from db import Database

d = Database()
website_src = os.path.abspath('website')
app = Flask(__name__, root_path=website_src)

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/init/<int:station>/<int:rowAmount>', methods=['GET', 'POST'])
def init_values(station, rowAmount):
  if station == 0:
    archive_data = d.execute("SELECT * FROM serial_data LIMIT %d " % rowAmount)
  else:
    archive_data = d.execute("SELECT * FROM serial_data WHERE id = %d" % station)
  return jsonify(archive_data)

@app.route('/info/<int:station>', methods=['GET', 'POST'])
def info(station):
  try: 
    values = d.read_db(station, 1)
    #print('from db:', values)
    return jsonify(values)
  except Exception as e:
    print(e)
    return 400

@app.route('/stations')
def hello_stations():
  return render_template('stations.html')

@app.route('/stations/<int:station>')
def station_table(station):
  #print('station %d' % station)
  return render_template('index.html', station=station)

@app.route('/data')
def data():
  return str(d.execute("SELECT * FROM serial_data"))

@app.route('/chart')
def chart():
  return render_template('chart_demo.html')

# only for external use in `test/` directory
def test_main():
  app.run(debug=True) 

  

if __name__ == "__main__":
  app.run(debug=True)
