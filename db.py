#!/usr/bin/env python3

import sqlite3
from connection import Connection
import time
import os
import sys  

SIM = os.getenv('SIM', None) is not None
READ = os.getenv('READ', None) is not None
WRITE = os.getenv('WRITE', None) is not None
CLEAR = os.getenv('CLEAR', None) is not None

class Database:
  def __init__(self, sim_mode=None):
    self.sim_mode = sim_mode is not None 
    self.serial_connection = Connection('/dev/ttyACM0', self.sim_mode)
    self.conn = sqlite3.connect('serial_archive.db', check_same_thread=False)
    self.cur = self.conn.cursor() 
    self.init_db()

  def create_table(self, table):
    try:
      self.cur.execute(table)
    except AttributeError:
      pass

  def init_db(self): 
    # two tables in the db
    if SIM:
      data_table = """CREATE TABLE IF NOT EXISTS sim_data (
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
    x = [v for k,v in data.items()]
    if SIM:
      sql = "INSERT INTO sim_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
    else:
      sql = "INSERT INTO serial_data VALUES (?,?,?,?,?,?,?,?)"
    try:
      self.cur.execute(sql, x)
    except sqlite3.OperationalError as e:
      print(__file__, e)
      sql = "INSERT INTO sim_data VALUES (?,?,?,?,?,?,?,?)"
      sql_data = (x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
      self.cur.execute(sql, sql_data)
    self.conn.commit()
    print('commited: ', x)

  def read_db(self, n, table=None):
    acc = []
    if table == None:
      if SIM:
        sql = "SELECT * FROM sim_data"
      else:
        sql = "SELECT * FROM serial_data"
    else:
      sql = "SELECT * FROM %s" % table
    for row in self.cur.execute(sql):
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
      db.write_db(5)
  if READ:
    # usage:
    # n -> returns last n elements
    # 0 -> returns whole database
    # ./db.py f 10 -> loop, 10 seconds of delay
    if len(sys.argv) > 2:
      a = sys.argv[-2]
      if a == 'f':
        d = sys.argv[-1]
        while(1): 
          print(db.read_db(1)) 
          time.sleep(5)
    else:
      a = sys.argv[-1]
      for x in db.read_db(int(a)):
        print(x, end='\n')
  if CLEAR:
    # usage:
    # ./db.py {table}
    # ./db.py sim_data
    table = sys.argv[1]
    db.execute("DELETE FROM %s;" % table) # doesn't work
    print(db.read_db(0, table))

