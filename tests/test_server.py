import unittest
import requests
import sys
import os
from pathlib import Path

parent_folder = os.path.basename(os.getcwd())
if parent_folder == 'tests':
  parent_dir = Path(os.getcwd()).parent
  sys.path.insert(1, parent_dir.__str__())

import serve
from utils.network import url_is_up

class TestServer(unittest.TestCase):
  def setup(self):
    serve.app.testing = True
    self.app = serve.app.test_client()
      
  def test_flask_startup(self):
    self.assertTrue(url_is_up("http://localhost:5000", "RERE"))

if __name__=="__main__":
  unitest.main() 
