#!/usr/bin/env python3
import sys
import os

class Configuration:
  """
  Usage information:
    
  ./config PORT MODE

  - PORT:

  port on linux should be something like /dev/ttyACM0
  on mac: /dev/tty.usbmodem101
  
  - MODE:

  mode by default is set to real-dummy which is for 
  data format that looks like this:
  [1.0, 1000.3, 124.23, 24.34, 61.57, 15.12, 71.3]

  """
  def __init__(self, arr):
    if len(arr) > 0:
      self.port = arr[0] 
      if self.port == 'find':
        self.port = self.find_port() 
      if len(arr) > 2:
        self.mode = arr[1]
      else:
        self.mode = "real-dummy"
    else:
      # change this if you want different values
      self.port = "/dev/ttyACM0"
      self.mode = "real-dummy"

    self.set_env()

  def set_env(self):
    os.environ['RERE-PORT'] = self.port
    if self.mode is not None:
      os.environ['RERE-MODE'] = self.mode
      
  def find_port(self):
    return os.popen('./tools/mac_find_port.sh').read().strip()

if __name__ == "__main__":
  arguments = sys.argv[1::]
  print(arguments)
  config = Configuration(arguments)
  print(os.environ)
  for e,v in os.environ.items():
    print(e,v)
  
