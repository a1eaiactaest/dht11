#!/usr/bin/env python3
from tqdm import tqdm
import unittest
import pytest
import time
import os
import sys
import tempfile

parent = os.path.basename(os.getcwd())
if parent == 'tests':
  sys.path.insert(0, '../utils')

from serial_ports import find_serial_port
from serial_ports import ArtificialSerial

def is_direct(dec):
  def decorator(func):
    if __name__ == "__main__":
      return func
    return pytest.fixture(func, scope="session", autouse=True)
  return decorator

@is_direct(pytest.fixture(scope="session", autouse=True))
def wait():
  print("*** Make sure to disconnect all arduino devices during this test ***") 
  pbar = tqdm(total=100)
  for i in range(100):
    pbar.update(n=1)
    time.sleep(.1)

class TestFindSerial(unittest.TestCase):
  def test_available(self):
    ports = find_serial_port()

if __name__ == "__main__":
  wait()
  unittest.main()
    
