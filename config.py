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

  use "find" as argv[1] to automatically find a port
  
  - MODE:

  mode by default is set to real-dummy which is for 
  data format that looks like this:
  [1.0, 1000.3, 124.23, 24.34, 61.57, 15.12, 71.3]

  """
  def __init__(self, arr):
    # config file is for default settings
    # check if config file exists
    if os.path.exists('rere.conf'):
      conf_file = open('rere.conf', 'r').read() 
      if not conf_file:
        self.write_file('rere.conf')
    else:
      self.write_file('rere.conf')
    
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
      self.port = self.find_port()
      self.mode = "real-dummy"

    self.set_env()

  def write_file(self, name):
    conf_file = open(name, 'w')
    conf_file.write('PORT=\n')
    conf_file.write('MODE=\n')
    conf_file.close()
    print('please edit %s/rere.conf' % os.getcwd())

  def set_env(self):
    os.environ['RERE-PORT'] = self.port
    if self.mode is not None:
      os.environ['RERE-MODE'] = self.mode
      
  def find_port(self):
    return os.popen('./tools/mac_find_port.sh').read().strip()

if __name__ == "__main__":
  arguments = sys.argv[1::]
  config = Configuration(arguments)
  print(config)
