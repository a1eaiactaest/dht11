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
from common.parser import parse_to_dict

from database import Database

DEBUG = os.getenv("DEBUG", None) is not None

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

if DEBUG:
  db_name = 'test'
else:
  db_name = 'archive_serial'

db = Database(db_name)

@cache
@app.route('/api/info/<int:station>')
def info(station: int) -> Union[str, int]:
  if station != 0:
    db_dump = db.read(station=station)
  else:
    db_dump = db.read(rows=1)
    print(db_dump)
  if db_dump is None:
    return 500
  else:
    jsoned_data = parse_to_dict(db_dump)
    return jsoned_data

if __name__ == "__main__":
  if DEBUG:
    # flask, dev server
    app.run(debug=True, host="0.0.0.0", port=1337)
  else:
    # wsgi, production server
    serve(app, host="0.0.0.0", port=1337)

