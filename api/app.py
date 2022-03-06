#!/usr/bin/env python3

import os
import time
from flask import Flask, jsonify
from flask_cors import CORS
from utils.serial_ports import generate_dd
from waitress import serve
import logging
import json

DEBUG = os.getenv("DEBUG", None) is not None

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

@app.route('/api/info')
def info():
  recv = str(generate_dd())
  if "Error" in recv:
    return 500
  else:
    data = recv.split(' ')
    formatted_data = {
      'time': int(time.time()),
      'id': data[0],
      'pres': data[1],
      'gas_res': data[2],
      'temp': data[3],
      'hum': data[4],
    }
    return json.dumps(formatted_data)

if __name__ == "__main__":
  if DEBUG:
    # flask 
    app.run(debug=True, port=1337)
  else:
    # wsgi production server
    serve(app, host="0.0.0.0", port=1337)

