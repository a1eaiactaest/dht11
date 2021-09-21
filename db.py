#!/usr/bin/env python3

import sqlite3
from connection import Connection
import time

class Database:
  def __init__(self):
    self.serial = Connection('/dev/ttyACM0')
    self.conn = sqlite3.connect('databases/values.db')
    self.init_database()

  def create_table(self, table):
    try:
      cur = self.conn.cursor()
      cur.execute(table)
    except Exception as e:
      print(e)

  def init_database(self):
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
    cur = self.conn.cursor() 
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
    cur.execute(sql, sql_data)
    self.conn.commit()
    print(data) 

if __name__ == "__main__":
  db = Database()
  serial_connection = Connection('/dev/ttyACM0')
  while (1):
    try:
      #time.sleep(5)
      x = serial_connection.read(False, True)
      db.append_td(x)
    except Exception as e:
      print(e)
    
