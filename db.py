#!/usr/bin/env python3

import sqlite3
from connection import Connection
import time
import os
import sys  

READ = os.getenv('READ', None) is not None
WRITE = os.getenv('WRITE', None) is not None
CLEAR = os.getenv('CLEAR', None) is not None
EXEC = os.getenv('EXEC', None) is not None

class Database:
  def __init__(self, name=None):
    self.serial_connection = Connection()
    if name == None:
      name = 'serial_archive.db' 
    self.conn = sqlite3.connect(name, check_same_thread=False)
    self.cur = self.conn.cursor() 
    self.init_db()

  def create_table(self, table):
    try:
      self.cur.execute(table)
    except AttributeError:
      pass

  def init_db(self): 
    data_table = """CREATE TABLE IF NOT EXISTS serial_data (
                    time      integer,
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
    sql = "INSERT INTO serial_data VALUES (?,?,?,?,?,?,?,?)"
    try:
      self.cur.execute(sql, x)
    except sqlite3.OperationalError as e:
      print(__file__, e)
      sql = "INSERT INTO serial_data VALUES (?,?,?,?,?,?,?,?)"
      sql_data = (x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
      self.cur.execute(sql, sql_data)
    self.conn.commit()
    print('commited: ', x)

  def read_db(self, station, n, table=None):
    acc = []
    if table == None:
      if station == 0: # station 0 for all stations
        sql = "SELECT * FROM serial_data"
      else:
        sql = "SELECT * FROM serial_data WHERE id = %d" % station
    else:
      if station == 0: # station 0 for all stations
        sql = "SELECT * FROM %s" % table
      else:
        sql = "SELECT * FROM %s WHERE id = %d" % (table, int(station))
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

  def execute(self, query):
    ret = [row for row in self.cur.execute(query)]
    self.conn.commit()
    return ret
  

if __name__ == "__main__":
  db = Database()
  if WRITE:
    while (1):
      #db.write_db(300) # every 5 minutes 
      db.write_db(10)
  if READ:
    # usage:
    # x -> which station, 0 for all stations w/o filtering
    # n -> returns last n elements, 0 for all elements
    # 'f' -> reading loop
    # READ=1 ./db.py x n 
    # READ=1 ./db.py 3 f 10 -> loop, 10 seconds of delay, read only from station 3
    station = int(sys.argv[1])
    if len(sys.argv) > 3:
      a = sys.argv[-2]
      if a == 'f':
        d = sys.argv[-1]
        while(1): 
          print(db.read_db(station, 1)) 
          time.sleep(15)
    else:
      a = int(sys.argv[-1])
      ret = db.read_db(station, a)
      for x in ret:
        print(x, end='\n')
  if CLEAR:
    # usage:
    # ./db.py {table}
    table = sys.argv[1]
    db.execute("DELETE FROM %s;" % table) # doesn't work
    print(db.read_db(0, 0, table)) # 0 for whole db, 0 for filtering off
  if EXEC:
    command = "SELECT * FROM serial_data ORDER BY time DESC LIMIT 10"
    print(db.execute(command))
