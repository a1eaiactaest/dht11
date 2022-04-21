#!/usr/bin/env python3

import os
import time
import logging
import json
from typing import Union
from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve

from common.cache import cache
from common.parser import parse_to_dict, parse_stations

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
@app.route('/api/<string:table>', methods=['GET', 'POST'])
def api_call(table: str) -> Union[str, int]:
  args = request.args
  print('reguest args:', args)

  if table == 'serial_data': 
    station = args.get('station')
    rows = args.get('rows')

    if station is None:
      station = 0
    # read one row by default
    if rows is None:
      rows = 1

    if station != 0:
      db_dump = db.read(station=int(station), table=table, rows=int(rows))
    else:
      db_dump = db.read(rows=int(rows))

  elif table == 'stations_index':
    db_dump = db.read(table=table, rows=-1)
      
  else:
    print(f"Table ({table}) doesn't exist. Returning 400")
    return 'Error 400' # Bad Request

  print('db_dump:', db_dump)
  if db_dump is None:
    return 'Error 500'
  else:
    if table == 'serial_data':
      if len(db_dump) == 1:
        return parse_to_dict(db_dump[0])
      else:
        ret = []
        for dp in db_dump:
          ret.append(parse_to_dict(dp))
        return jsonify(ret)

    elif table == 'stations_index':
      return parse_stations(db_dump)

if __name__ == "__main__":
  if DEBUG:
    # flask, dev server
    app.run(debug=True, host="0.0.0.0", port=1337)
  else:
    # wsgi, production server
    serve(app, host="0.0.0.0", port=1337)

