#!/usr/bin/env python3
import os
import sys

from flask import Flask, render_template, jsonify, request

from utils.network import init_db

d = init_db()
website_src = os.path.abspath('rere-website')
app = Flask(__name__, root_path=website_src)

parse_stations = lambda x: int(x[0])

@app.route('/')
def hello():
  stations = sorted(list(map(parse_stations, d.get_stations())))
  print(stations)
  return render_template('index.html', stations=stations)

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

@app.route('/stations')
def hello_stations():
  stations = sorted(list(map(parse_stations, d.get_stations())))
  print(stations)
  return render_template('stations.html', stations=stations)

@app.route('/info')
def hello_info():
  return 'Endpoint /info not implemented yet'

@app.route('/learn')
def hello_learn():
  return render_template('learn/index.html')

@app.route('/learn/traszka-zwyczajna')
def hello_traszka():
  return render_template('learn/traszka-zwyczajna.html')

@app.route('/learn/ropucha-zielona')
def hello_ropucha():
  return render_template('learn/ropucha-zielona.html')

@app.route('/stations/<int:station>')
def station_table(station):
  return render_template('station.html', station=station)

@app.route('/api')
def hello_api():
  return 'Endpoint /api not implemented yet'

@app.route('/data')
def data():
  return str(d.execute("SELECT * FROM serial_data"))

# only for external use in `test/` directory
def test_method():
  # this will suppress output
  import logging
  log = logging.getLogger('werkzeug')
  log.setLevel(logging.ERROR)
  app.run(debug=False) 

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
