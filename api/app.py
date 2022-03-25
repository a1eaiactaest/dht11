#!/usr/bin/env python3

import os
import time
import logging
import json
from typing import Union
from flask import Flask, jsonify
from flask_cors import CORS
from waitress import serve

from common.cache import cache
from common.parser import parse
from common.serial_ports import generate_dd, Serial

DEBUG = os.getenv("DEBUG", None) is not None

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

serial_conn = Serial()

@cache
@app.route('/api/info')
def info() -> Union[str, int]:
  recv = serial_conn.read() # this later should be in database worker
  if recv is None:
    return 500
  else:
    json_data = parse(recv)
    return json_data

if __name__ == "__main__":
  if DEBUG:
    # flask, dev server
    app.run(debug=True, host="0.0.0.0", port=1337)
  else:
    # wsgi, production server
    serve(app, host="0.0.0.0", port=1337)

