#!/usr/bin/env python3

import serial
import time
import sys
from flask import Flask, render_template

app = Flask(__name__)

port = sys.argv[1]
s = serial.Serial(port, 9600)
s.reset_input_buffer()

@app.route('/')
def hello():
  return render_template('index.html')

def info():
  while (1):
    try: 
      s_bytes = s.readline()
      decoded = s_bytes[0:len(s_bytes)-2].decode("utf-8")
      v = [float(x) for x in decoded.split(' ')]
      print(v)

    except Exception as e:
      print(e)
      break


if __name__ == "__main__":
  app.run(debug=True)
