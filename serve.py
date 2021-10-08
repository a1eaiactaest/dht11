#!/usr/bin/env python3

import os
import sys
import json
import threading
import time
from flask import Flask, render_template, jsonify, request
from db import Database

SIM = os.getenv('SIM', None) is not None

class Thread(object):
  def __init__(self, delay=100000):
    self.acc = 0
    self.delay = delay
    t = threading.Thread(target=self.run, args=())
    t.daemon = True
    t.start()

  def run(self):
    while(1):
      d.write_db(900, True)

if SIM:
  d = Database('SIM')
else:
  d = Database()

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/init')
def init_values():
  archive_data = d.execute("SELECT * FROM serial_data")
  return jsonify(archive_data)

@app.route('/info', methods=['GET'])
def info():
  try: 
    values = d.read_db(1)
    print(values)
    return jsonify(values)
  except Exception as e:
    print(e)
    return 400

@app.route('/data')
def data():
  return str(d.execute("SELECT * FROM serial_data"))

if __name__ == "__main__":
  app.run(debug=True)
