#!/usr/bin/env python3

import serial
import time
import sys
import csv
import json
import datetime
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

port = sys.argv[1]
s = serial.Serial(port, 9600)
s.reset_input_buffer()

f = open('data.json', 'w')

def serialize(t, hum, tem, hic):
  ret = json.dumps({'time': t, 'humidity': hum, 'temperature': tem, 'heat index': hic})
  return ret 
  
def write(dest, data):
  dest.write(data) 
  dest.write('\n')

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/info', methods=['GET'])
def info():
  try: 
    s_bytes = s.readline()
    decoded = s_bytes[0:len(s_bytes)-2].decode("utf-8")
    v = [float(x) for x in decoded.split(' ')]
    t = str(datetime.datetime.now())
    ret = {'time': t, 'humidity': v[0], 'temp': v[1], 'hic': v[2]}
    print(ret)
    write(f, serialize(t, v[0], v[1], v[2]))
    print(t, ' - json data updated')
    return jsonify(ret)
  except Exception as e:
    print(e)
    return 400

if __name__ == "__main__":
  app.run(debug=True)
