#!/usr/bin/env python3

import os
import sys
import json
import threading
import time
from flask import Flask, render_template, jsonify, request
from db import Database

d = Database()

class Thread(object):
  def __init__(self, delay=1):
    self.delay = delay
    t = threading.Thread(target=self.run, args=())
    t.daemon = True
    t.start()

  def run(self):
    while(1):
      d.write_db(10)

app = Flask(__name__)
tr = Thread()


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
    return jsonify(values)
  except Exception as e:
    print(e)
    return 400

@app.route('/data')
def data():
  return str(d.execute("SELECT * FROM serial_data"))

if __name__ == "__main__":
  app.run(debug=True)
