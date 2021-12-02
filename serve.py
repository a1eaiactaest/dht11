#!/usr/bin/env python3
import os
import sys

from flask import Flask, render_template, jsonify, request

from utils.network import init_db

d = init_db()
website_src = os.path.abspath('rere-website')
app = Flask(__name__, root_path=website_src)

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/init/<int:station>', methods=['GET', 'POST'])
def init_values(station):
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
    #print('from db:', values)
    return jsonify(values)
  except Exception as e:
    print(e)
    return 400

@app.route('/stations')
def hello_stations():
  return render_template('index.html')

@app.route('/stations/<int:station>')
def station_table(station):
  #print('station %d' % station)
  return render_template('station.html', station=station)

@app.route('/data')
def data():
  return str(d.execute("SELECT * FROM serial_data"))

# only for external use in `test/` directory
def test_main():
  app.run(debug=True) 

if __name__ == "__main__":
  app.run(debug=True)
