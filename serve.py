#!/usr/bin/env python3

import os
import sys
import json
import threading
import time
from flask import Flask, render_template, jsonify, request
from db import Database

SIM = os.getenv('SIM', None) is not None

d = Database(SIM)

app = Flask(__name__)

@app.route('/')
def hello():
  if SIM:
    return render_template('sim.html')
  else:
    return render_template('notsim.html')

@app.route('/init')
def init_values():
  archive_data = d.execute("SELECT * FROM serial_data")
  return jsonify(archive_data)

@app.route('/info', methods=['GET'])
def info():
  try: 
    values = d.read_db(1)
    print('from db:', values)
    return jsonify(values)
  except Exception as e:
    print(e)
    return 400

@app.route('/stations')
def hello_stations():
  return render_template('stations.html')

@app.route('/data')
def data():
  return str(d.execute("SELECT * FROM serial_data"))

if __name__ == "__main__":
  app.run(debug=True)
