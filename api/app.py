#!/usr/bin/env python3

import os
import time
from flask import Flask, jsonify
from flask_cors import CORS
from utils.serial_ports import generate_dd, Serial
from waitress import serve
import logging
import json

DEBUG = os.getenv("DEBUG", None) is not None

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

serial_conn = Serial()

@app.route('/api/info')
def info():
  # dummy
  #recv = str(generate_dd())

  recv = serial_conn.read() # this later should be in database worker
  if recv is None:
    return 500
  else:
    formatted_data = {
      'time': int(time.time()),
      'id': recv[0],
      'pres': recv[1],
      'gas_res': recv[2],
      'temp': recv[3],
      'hum': recv[4],
    }
    return json.dumps(formatted_data)

if __name__ == "__main__":
  if DEBUG:
    # flask, dev server
    app.run(debug=True, host="0.0.0.0", port=1337)
  else:
    # wsgi, production server
    serve(app, host="0.0.0.0", port=1337)

