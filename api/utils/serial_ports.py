#!/usr/bin/env python3
import os 
from random import randrange, choice 
import platform
from shutil import which
import serial
import pty
import threading
import time
from typing import Union

from utils.cache import cache

DEBUG = os.getenv("DEBUG") is not None

@cache
def find_serial_port() -> str:
  """
  Search for serial port in /dev, works on Mac and Linux.
  Returns absolute path as a string.
  """
  devices = os.listdir("/dev")
  if platform.system() == "Darwin":
    ports = [f"/dev/{port}" for port in devices if "tty.usb" in port]
  elif platform.system() == "Linux":
    ports = [f"/dev/{port}" for port in devices if "ttyACM" in port or "ttyUSB" in port]

  if len(ports) > 1:
    raise Exception("More than one serial port has been found")
  elif len(ports) == 1: 
    return ports[0]
  else:
    raise Exception("No serial ports found")

@cache
def generate_dd() -> str:
  """
  Return pseudo random array of dummy data. 
  See `../dummy/dummy.ino`
  """
  station = choice([3,5,11,103,69,420,1337])
  pres = randrange(900, 1000)
  gas_res = randrange(0,255)
  a_temp = randrange(15,25)
  a_hum = randrange(40,60)
  gd_temp = randrange(0,10)
  gd_hum = randrange(60,100)

  return ' '.join(list(map(str, [station, pres, gas_res, a_temp, a_hum, gd_temp, gd_hum])))

class Serial:
  """
  connect to phisical serial port and scrape data
  
  -- example data samples:
    -- normal

      "103 1009.00 120.00 20.00 52.00 2.00 87.00\n"

      
    -- error message
  type hint for constructor:
    https://peps.python.org/pep-0484/#the-meaning-of-annotations
  """
  def __init__(self, port_name=None, baud=9600) -> None:
    if os.getenv("PORT", None) is None:
      if port_name is None:
        port_name = find_serial_port()     
    else:
      port_name = os.getenv("PORT")

    self.port_name = port_name
    self.baud = baud
    self.connection = self.connect()

    print(self.port_name)

  def connect(self) -> serial.Serial:
    connection = serial.Serial(self.port_name, self.baud) 
    connection.reset_input_buffer()
    return connection

  @cache
  def read(self) -> Union[list, None]:
    bline = self.connection.readline()
    line = self.parse(bline)
    if "Error:" in line:
      print(int(time.time()), ' '.join(line)) 
      return 
    return line

  def decode(self, bytes_object: bytes) -> str:
    """
    Takes bytes object as a argument.
    Returns UTF-8 string
    """
    return bytes_object.decode("utf-8")

  def parse(self, line: bytes) -> list:
    # take bytes object as argument 
    # strip and split line into separate values, return array
    line_decoded = self.decode(line)
    return line_decoded.strip().split(' ')

  def validate(line: list) -> bool:
    raise NotImplementedError

  def integrity_check(self):
    assert self.port_name == self.connection.name, "var:port_name and var:connection.name are mismatched"


if __name__ == "__main__":
  S = Serial()
  while True:
    data_recv = S.read()
    if data_recv:
      print(data_recv)
    time.sleep(2)
