#!/usr/bin/env python3

import os
DEBUG = os.getenv("DEBUG", None) is not None
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
    time.sleep(2) # sleep 2 seconds before reading

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

  def read(self, DEBUG=False):
    s_bytes = self.s.readline()
    # cut last 3 chars, change to 2 if running dht11 example, 
    # this one is for sim one
    bytes_decoded = s_bytes[0:len(s_bytes)-3].decode("utf-8")
    val = [float(v) for v in bytes_decoded.split(" ")]
    ct = str(datetime.datetime.now())
    try:
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
    c.read(True) 

