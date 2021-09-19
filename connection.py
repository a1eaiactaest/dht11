#!/usr/bin/env python3

# SIM:
# [1.0, 1000.3, 124.23, 24.34, 61.57, 15.12, 71.3, 69.42, 42.07, 45.65, 0.0]

import os
DEBUG = os.getenv("DEBUG", None) is not None
SIM = os.getenv("SIM", None) is not None
import serial
import time
import sys
import datetime
import json

class Connection:
  def __init__(self, port):
    self.port = port #/dev/tty*
    self.s = serial.Serial(port, 9600)
    self.s.reset_input_buffer()

    time.sleep(2) # sleep 2 seconds before reading, otherwise it bugs

    self.f = open('data.json', 'a')
    self.x = []

  def reset(self):
    self.x = []

  def write(self, data):
    self.f.write(data) 
    self.f.write('\n')

  def serialize(self, d):
    self.x.append(d)
    packed = json.dumps(self.x)
    #print(packed)
    return packed 

  def read(self, DEBUG=False, SIM=True):
    s_bytes = self.s.readline()
    if SIM:
      bytes_decoded = s_bytes[0:len(s_bytes)-3].decode("utf-8")
    else:
      bytes_decoded = s_bytes[0:len(s_bytes)-2].decode("utf-8")
    val = [float(v) for v in bytes_decoded.split(" ")]
    ct = str(datetime.datetime.now())
    try:
      if SIM:
        ret = {"time": ct,
               "id": val[0],
               "pres": val[1],
               "gas_res": val[2],
               "a_temp": val[3],
               "a_hum": val[4],
               "gd_temp": val[5],
               "gd_hum": val[6],
               "gps_lat": val[7],
               "gps_lon": val[8],
               "gps_angle": val[9],
               "gps_speed": val[10]}

      else:
        ret = {'time': ct, 'humidity': val[0], 'temp': val[1], 'hic': val[2]}
      if DEBUG:
        print(ret)
    except IndexError:
      print('error occured running again')
      return self.read() # don't know if works
    self.write(self.serialize(ret))
    self.reset()
    return ret

if __name__ == "__main__":
  if len(sys.argv) < 2:
    c = Connection('/dev/ttyACM0')
  else:
    c = Connection(sys.argv[1])
  while(1):
    time.sleep(1)
    c.read(True, SIM) 

