#!/usr/bin/env python3 

import os
import sys
import time
import sqlite3
from typing import Union, Optional

from utils.basedir import BASEDIR, DATABASES

class Database:
  def __init__(self, name: str) -> None:
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
        time    integer,
        id      integer, 
        pres    real,
        gas_res real,
        air_te  real, 
        air_hu  real,
        gnd_te  real,
        gnd_hu  real
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
    raise NotImplementedError

  def write(self, data: list, delay: Optional[int] = None) -> None:
    raise NotImplementedError

  def close(self, delay: Optional[int] = None) -> None:
    if delay is not None:
      time.sleep(delay)
    self.db_conn.close()

if __name__ == "__main__":
  database = Database('test')
  print(database.stations) 
