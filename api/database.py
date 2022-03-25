#!/usr/bin/env python3 

import os
import sys
import time
import sqlite3
from typing import Union, Optional, List

from common.cache import cache
from common.basedir import BASEDIR, DATABASES

class Database:
  def __init__(self, name: str, DEBUG: Optional[bool] = False) -> None:
    self.name = name 
    self.db_conn, self.db_cur = self.connect_db()
    self.stations = list(set(self.execute("SELECT * FROM stations_index")))

  def connect_db(self) -> Union[sqlite3.Connection, sqlite3.Cursor]:
    if not os.path.exists(DATABASES):
      os.mkdir(DATABASES)

    db_conn = sqlite3.connect(f"{DATABASES}/{self.name}.db", check_same_thread=False)
    db_cur = db_conn.cursor()

    sql = """
      CREATE TABLE IF NOT EXISTS serial_data (
        time      integer,
        id        integer, 
        air_pres  real,
        voc       real,
        air_temp  real, 
        air_hum   real,
        gnd_temp  real,
        gnd_hum   real
      );

      CREATE TABLE IF NOT EXISTS stations_index (
        id      integer primary key,
        UNIQUE(id)
      );
    """
    db_cur.executescript(sql)

    return db_conn, db_cur

  def execute(self, query: str) -> Optional[list]:
    db_out = list(self.db_cur.execute(query))
    self.db_conn.commit()
    if db_out is None:
      return None
    return db_out
  
  def add_row(self, data: list) -> None:
    if len(data) != 8:
      return 

    station = data[1]
    if station not in self.stations:
      try:
        if type(station) == int:
          self.stations.add(station)
          self.execute(f"INSERT INTO stations_index VALUES ({station})")
          print(f"({station}) added to the station_index database: ")
          print(self.stations)
      except sqlite3.IntegrityError:
        print(f"({station}) alread is in station_index database.")
    
    try: 
      sql = "INSERT INTO serial_data VALUES (?,?,?,?,?,?,?,?)"
      self.db_cur.execute(sql, data)
      self.db_conn.commit()
      print(f"commit: {data}")
    except sqlite3.OperationalError as e:
      raise RuntimeError(f"sql operation has failed. sql: '{sql}', error {e}")

  def write(self, data: list, delay: Optional[int] = None) -> None:
    self.add_row(data)
    if delay is not None:
      time.sleep(delay)

  def read(self, rows: int = -1, station: Optional[int] = None, table: Optional[str] = None) -> list:
    #raise NotImplementedError
    if table == None:
      if station == None:
        sql = f"SELECT * FROM serial_data LIMIT {rows};"
      else:
        sql = f"SELECT * FROM serial_data WHERE id = {station} LIMIT {rows};"
    else:
      if station == None:
        sql = f"SELECT * FROM {table} LIMIT {rows};"
      else:
        sql = f"SELECT * FROM {table} WHERE id = {station} LIMIT {rows};"

    ret = []
    for row in self.db_cur.execute(sql):
      ret.append(row)

    return ret

  def close(self, delay: Optional[int] = None) -> None:
    if delay is not None:
      time.sleep(delay)
    self.db_conn.close()

if __name__ == "__main__":
  database = Database('test')
