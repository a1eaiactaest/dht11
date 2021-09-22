#!/usr/bin/env python3

import os
SIM = os.getenv("SIM", None) is not None
import sys
import json
from flask import Flask, render_template, jsonify, request
from db import Database

app = Flask(__name__)

d = Database()

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/table')
def hello_table():
  return render_template('table.html')

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
  return open('data.json').read()

if __name__ == "__main__":
  app.run(debug=True)
