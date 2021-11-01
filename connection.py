#!/usr/bin/env python3

# example:
# [1.0, 1000.3, 124.23, 24.34, 61.57, 15.12, 71.3]

import os
DEBUG = os.getenv("DEBUG", None) is not None
import serial
import time
import sys
import datetime
import json

class Connection:
  def __init__(self, port=None):
    if port == None:
      self.port = os.eviron['RERE_PORT']
    else:
      self.port = port #/dev/tty*
    self.s = serial.Serial(port, 9600)
    self.s.reset_input_buffer()

    time.sleep(2) # sleep 2 seconds before reading, otherwise it bugs
    self.reset()

  def reset(self):
    self.x = []

  def serialize(self, d):
    self.x.append(d)
    packed = json.dumps(self.x)
    #print(packed)
    return packed 

  def read(self, DEBUG=False):
    s_bytes = self.s.readline()
    try:
      bytes_decoded = s_bytes[0:len(s_bytes)-3].decode("utf-8")
      val = [float(v) for v in bytes_decoded.split(" ")]
    except ValueError as e:
      print(e)
    ct = str(datetime.datetime.now())[:-7]
    try:
      ret = {"time": ct,
             "id": int(val[0]),
             "pres": val[1],
             "gas_res": val[2],
             "a_temp": val[3],
             "a_hum": val[4],
             "gd_temp": val[5],
             "gd_hum": val[6]}
      if DEBUG:
        print(ret)
    except Exception as e:
      print(e)
      return self.read()
    self.reset()
    return ret

if __name__ == "__main__":
  if len(sys.argv) < 2:
    c = Connection('/dev/ttyACM0')
  else:
    c = Connection(sys.argv[1])
  while(1):
    time.sleep(1)
    c.read(True) 
    c.s.reset_output_buffer()

