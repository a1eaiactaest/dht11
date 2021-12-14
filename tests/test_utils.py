#!/usr/bin/env python3
import unittest
import pytest

import os
import sys

parent = os.path.basename(os.getcwd())
if parent == 'tests':
  sys.path.insert(0, '../utils')

from serial_ports import find_serial_port
from serial_ports import ArtificialSerial

class TestFindSerial(unittest.TestCase):
  
  print('NAME:',__name__)
  def test_available(self):
    print('NAME:',__name__)
    atty = ArtificialSerial()
    ports = find_serial_port()
    print(ports)

    
def is_direct(dec):
  def decorator(func):
    if __name__ == "__main__":
      return func
    return pytest.fixture(func, scope="session", autouse=True)
  return decorator

@is_direct(pytest.fixture(scope="session", autouse=True))
def wait():
  print("Make sure to disconnect all arduino devices during this test") 
  input("Press [enter] to continue")

if __name__ == "__main__":
  wait()
  unittest.main()
    
