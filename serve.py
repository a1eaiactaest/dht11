#!/usr/bin/env python3

import os
SIM = os.getenv("SIM", None) is not None
import sys
import json
from flask import Flask, render_template, jsonify, request
from connection import Connection

app = Flask(__name__)

c = Connection(sys.argv[1])

def serialize(t, hum, tem, hic):
  ret = json.dumps({'time': t, 'humidity': hum, 'temperature': tem, 'heat index': hic})
  return ret 
  
def write(dest, data):
  dest.write(data); dest.write('\n') 

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/table')
def hello_table():
  return render_template('table.html')

@app.route('/info', methods=['GET'])
def info():
  try: 
    values = c.read(True)
    return jsonify(values)
  except Exception as e:
    print(e)
    return 400

@app.route('/data')
def data():
  return open('data.json').read()

if __name__ == "__main__":
  app.run(debug=True)
