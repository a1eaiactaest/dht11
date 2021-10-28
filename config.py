#!/usr/bin/env python3
import sys
import os

class Configuration:
  def __init__(self, arr):
    if len(arr) > 0:
      self.port = arr[0] 
      self.mode = arr[1]
    else:
      # change this if you want different values
      self.port = "/dev/ttyACM0"
      self.mode = "real-dummy"

    self.set_env()

  def set_env(self):
    os.environ['RERE-PORT'] = self.port
    os.environ['RERE-MODE'] = self.mode
    

if __name__ == "__main__":
  arguments = sys.argv[1::]
  print(arguments)
  config = Configuration(arguments)
  print(os.environ)
  for e,v in os.environ.items():
    print(e,v)
  
