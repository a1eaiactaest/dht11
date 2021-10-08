#!/usr/bin/env python3

import sqlite3
from connection import Connection
import time
import os

SIM = os.getenv('SIM', None) is not None

READ = os.getenv('READ', None) is not None
WRITE = os.getenv('WRITE', None) is not None
CLEAR = os.getenv('CLEAR', None) is not None

class Database:
  def __init__(self, sim_mode):
    self.sim_mode = sim_mode is not None 
    if self.sim_mode:
      self.serial_connection = Connection('/dev/ttyACM0', True)
    else:
      self.serial_connection = Connection('/dev/ttyACM0', False)
    self.conn = sqlite3.connect('serial_archive.db', check_same_thread=False)
    self.cur = self.conn.cursor() 
    self.init_db()

  def create_table(self, table):
    try:
      self.cur.execute(table)
    except AttributeError:
      pass

  def init_db(self):
    if SIM:
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
    else:
      data_table = """CREATE TABLE IF NOT EXISTS serial_data (
                      time      text,
                      id        integer, 
                      pres      real,
                      gas_res   real,
                      a_temp    real,
                      a_hum     real,
                      gd_temp   real,
                      gd_hum    real);"""

    self.create_table(data_table)

  def append_td(self, data: dict):
    if SIM:
      sql = "INSERT INTO serial_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
    else:
      sql = "INSERT INTO serial_data VALUES (?,?,?,?,?,?,?,?)"
    sql_data = [v for k,v in data.items()]
    print(sql_data)
    self.cur.execute(sql, sql_data)
    self.conn.commit()

  def read_db(self, n):
    acc = []
    for row in self.cur.execute('SELECT * FROM serial_data'):
      acc.append(row)
    if n == 0:
      return acc
    else:
      return acc[len(acc)-n:len(acc)]

  def write_db(self, delay_minutes, debug=False): 
    x = self.serial_connection.read()
    self.append_td(x)
    if debug:
      print("\n%s - data has been written to the database" % (x['time']))
    time.sleep(delay_minutes)

  def execute(self, q):
    return [row for row in self.cur.execute(q)]


if __name__ == "__main__":
  if SIM:
    db = Database(True)
  else:
    db = Database()
  if WRITE:
    while (1):
      #db.write_db(300) # every 5 minutes 
      db.write_db(10)
  if READ:
    # usage:
    # n -> returns last n elements
    # 0 -> returns whole database
    import sys  
    n = int(sys.argv[-1])
    for x in db.read_db(n):
      print(x, end='\n')
  if CLEAR:
    db.execute("DELETE FROM serial_data;") # doesn't work


