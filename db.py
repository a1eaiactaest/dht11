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

    self.stations = set(self.execute("SELECT * FROM stations"))

  def create_table(self, table):
    try:
      self.cur.execute(table)
    except AttributeError:
      pass

  def init_db(self): 
    sql = """CREATE TABLE IF NOT EXISTS serial_data (
                    time      integer,
                    id        integer, 
                    pres      real,
                    gas_res   real,
                    a_temp    real,
                    a_hum     real,
                    gd_temp   real,
                    gd_hum    real);
                    
                    CREATE TABLE IF NOT EXISTS stations (
                    id        integer primary key,
                    UNIQUE(id));
                    """

    self.cur.executescript(sql)

  def append_td(self, data: dict):
    x = [v for k,v in data.items()]

    station = x[1]
    if station not in self.stations:
      try:
        self.stations.add(station)
        self.execute("INSERT INTO stations VALUES (%d)"%station)
        print("added station %d to the database"%station)
      except sqlite3.IntegrityError:
        print("station %d already is in the database"%station)
    
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
    if ret is None:
      return None
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
    table = sys.argv[1]
    station = int(sys.argv[2])
    n = int(sys.argv[3])
    print(db.read_db(station, n, table=table)) 

  if CLEAR:
    # usage:
    # ./db.py {table}
    table = sys.argv[1]
    db.execute("DELETE FROM %s;" % table) # doesn't work
    print(db.read_db(0, 0, table)) # 0 for whole db, 0 for filtering off

  if EXEC:
    # important! argument needs to be in " "
    command = str(' '.join(sys.argv[1:]))
    print(db.execute(command))
