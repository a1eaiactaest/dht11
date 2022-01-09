#!/usr/bin/env python3

# example:
# [1.0, 1000.3, 124.23, 24.34, 61.57, 15.12, 71.3]

import os
import serial
import time
import sys
import datetime
import json
import logging


DEBUG = os.getenv("DEBUG", None) is not None
PTY = os.getenv("ART", None) is not None

class Connection:
  def __init__(self, port=None):
    if not PTY:
      if port == None:
        try:
          self.port = os.environ['RERE_PORT']
        except KeyError:
          #print('Set RERE_PORT environmental variable')
          #exit
          self.port = serial_ports.find_serial_port()
      else:
        self.port = port #/dev/tty*
      self.s = serial.Serial(self.port, 9600)
      self.s.reset_input_buffer()

    else:
      from utils import Seriald
      self.s  = Seriald()

    logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", filename='error.log', level=logging.ERROR)

    time.sleep(2) # sleep 2 seconds before reading, otherwise it bugs
    self.reset()

  def reset(self):
    self.x = []

  def serialize(self, d):
    self.x.append(d)
    packed = json.dumps(self.x)
    return packed 

  def read(self, DEBUG=False):
    if PTY:
      bytes_decoded = self.s.read().strip()
    else:
      s_bytes = self.s.readline().strip()
      bytes_decoded = s_bytes[0:len(s_bytes)-3].decode("utf-8")
      if "Error" in s_bytes.decode("utf-8"):
        logging.error(s_bytes.decode("utf-8").strip())
        return self.read()
    try:
      val = [float(v) for v in bytes_decoded.split(" ")]
    except ValueError as e:
      return self.read()
    ct = int(time.time())
    try:
      ret = {"time": ct,
             "id": int(val[0]),
             "pres": val[1],
             "gas_res": val[2],
             "a_temp": val[3], "a_hum": val[4],
             "gd_temp": val[5],
             "gd_hum": val[6]}
      if DEBUG:
        print(ret)
    except Exception as e:
      logging.error("ValueError: when trying to create dict")
      return self.read()

    self.reset()
    return ret

if __name__ == "__main__":
  if len(sys.argv) < 2:
    c = Connection()
  else:
    c = Connection(sys.argv[1])
  while(1):
    time.sleep(2)
    c.read(True) 
    c.s.reset_output_buffer()

