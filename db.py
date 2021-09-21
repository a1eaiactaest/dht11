#!/usr/bin/env python3

import sqlite3
from connection import Connection
import time
import os

READ = os.getenv('READ', None) is not None
WRITE = os.getenv('WRITE', None) is not None

class Database:
  def __init__(self):
    self.serial_connection = Connection('/dev/ttyACM0')
    self.conn = sqlite3.connect('databases/values.db')
    self.init_db()
    self.cur = self.conn.cursor() 

  def create_table(self, table):
    try:
      self.cur.execute(table)
    except AttributeError:
      pass

  def init_db(self):
    data_table = """CREATE TABLE IF NOT EXISTS serial_data (
                    time      text,
                    id        integer, 
                    pres      real,
                    gas_res   real,
                    a_temp    real,
                    a_hum     real,
                    gd_temp   real,
                    gd_hum    real,
                    gps_lat   real,
                    gps_lon   real,
                    gps_angle real,
                    gps_speed real);"""
    self.create_table(data_table)

  def append_td(self, data: dict):
    sql = "INSERT INTO serial_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
    sql_data = [data['time'],
                data['id'],
                data['pres'],
                data['gas_res'],
                data['a_temp'],
                data['a_hum'],
                data['gd_temp'],
                data['gd_hum'],
                data['gps_lat'],
                data['gps_lon'],
                data['gps_angle'],
                data['gps_speed']]
    self.cur.execute(sql, sql_data)
    self.conn.commit()

  def read_db(self, n):
    acc = []
    for row in self.cur.execute('SELECT * FROM serial_data'):
      #print(row)
      acc.append(row)
    # last 5
    if n == 0:
      for dataset in acc:
        print(dataset)
    else:
      for dataset in acc[len(acc)-n:len(acc)]:
        print(dataset)
      

  def write_db(self):
    try:
      # true for SIM mode
      time.sleep(5)
      x = self.serial_connection.read(False, True) 
      self.append_td(x)
      print("%s - data has been written to the database" % x['time'])
    except Exception as e:
      print(e)


if __name__ == "__main__":
  db = Database()
  if WRITE:
    while (1):
      db.write_db() 
  if READ:
    # usage:
    # n -> returns last n elements
    # 0 -> returns whole database
    db.read_db(5)
