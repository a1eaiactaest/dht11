#!/usr/bin/env python3
import os

from flask import Flask, jsonify

from utils.network import init_db

d = init_db()
app = Flask(__name__)

parse_stations = lambda x: int(x[0])

@app.route('/init/<int:station>/<int:rowAmount>', methods=['GET', 'POST'])
def init_values(station,rowAmount):
  rowAmount = 100
  if station == 0:
    sql = """
    SELECT onlyN.*
    FROM (SELECT *
          FROM serial_data
          ORDER BY time
          DESC
          ) onlyN
    LIMIT %d
    """ % rowAmount
    archive_data = d.execute(sql)[::-1] # reverse
  else:
    sql = """
    SELECT onlyN.*
    FROM (SELECT *
          FROM serial_data
          WHERE id = %d
          ORDER BY time 
          DESC
          ) onlyN
    LIMIT %d
    """ % (station, rowAmount)
    archive_data = d.execute(sql)[::-1] # reverse
  return jsonify(archive_data)

@app.route('/info/<int:station>', methods=['GET', 'POST'])
def info(station):
  try: 
    values = d.read_db(station, 1)
    return jsonify(values)
  except Exception as e:
    print(e)
    return 400

@app.route('/info')
def hello_info():
  return 'Endpoint /info not implemented yet'

@app.route('/api')
def hello_api():
  return 'Endpoint /api not implemented yet'

@app.route('/data')
def data():
  return str(d.execute("SELECT * FROM serial_data"))

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
