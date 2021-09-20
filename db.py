#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('databases/values.db')



def create_table(table):
  c = conn.cursor()
  c.execute(table)

def init_database():
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
  create_table(data_table)

if __name__ == "__main__":
  init_database()
  
