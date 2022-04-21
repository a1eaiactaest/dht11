#!/usr/bin/env python3 

import os
import sys
import time
import sqlite3
from typing import Union, Optional, List, Any

from common.cache import cache
from common.basedir import BASEDIR, DATABASES
from common.serial_ports import Serial
from common.parser import parse_to_list, pretty_db_dump

class Database:
  def __init__(self, name: str, DEBUG: Optional[bool] = False) -> None:
    self.name = name 
    self.db_conn, self.db_cur = self.connect_db()
    self.stations = list(set(self.execute("SELECT * FROM stations_index")))
    print(self.stations)

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
      print('length error')
      return 

    station = data[1]
    print('station:', station)
    if station not in self.stations:
      try:
        self.stations.append(station)
        self.execute(f"INSERT INTO stations_index VALUES ({station})")
        print(f"({station}) added to the stations_index database: ")
        print(self.stations)
      except sqlite3.IntegrityError:
        print(f"({station}) already is in stations_index database.")
    
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
        sql = f"SELECT * FROM serial_data ORDER BY time DESC LIMIT {rows};"
      else:
        sql = f"SELECT * FROM serial_data WHERE id = {station} ORDER BY time DESC LIMIT {rows};"
    elif table == 'stations_index':
      sql = f"SELECT * FROM stations_index"
    else:
      if station == None:
        sql = f"SELECT * FROM {table} ORDER BY time DESC LIMIT {rows};"
      else:
        sql = f"SELECT * FROM {table} WHERE id = {station} ORDER BY time DESC LIMIT {rows};"

    db_dump = self.db_cur.execute(sql).fetchall()
    if len(db_dump) > 1:
      print("**** HERE *****")
      ret = []
      for row in db_dump:
        ret.append(row)
      return ret
    else:
      return list(db_dump)

  def close(self, delay: Optional[int] = None) -> None:
    if delay is not None:
      time.sleep(delay)
    self.db_conn.close()

def background_worker(database_object: Database, WRITE: bool = False, READ: bool = False, **kwargs: dict[str, Any]) -> None:
  if kwargs:
    for arg in zip(kwargs, kwargs.values()):
      print(arg)
      if arg[0] == 'table':
        table = arg[1]
      else:
        table = None

      if arg[0] == 'station':
        station = arg[1]
      else:
        station = None

      if arg[0] == 'rows':
        rows = arg[1]
      else:
        rows = -1

  print(table, station, rows)

  if READ:
    # call database_object.read() or smth
    db_dump = database_object.read(rows, station, table)
    pretty_db_dump(db_dump)

  if WRITE:
    # read serial data, call database_object.write()
    serial_connection = Serial()
    while True:
      serial_data = serial_connection.read()
      parsed_line = parse_to_list(serial_data)
      print(parsed_line)
      database_object.write(parsed_line)

if __name__ == "__main__":
  database = Database('test')
  #background_worker(database, table='serial_data', READ=True, rows=1) 
  background_worker(database, table='serial_data', WRITE=True)
