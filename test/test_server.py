import unittest
import sys

sys.path.insert(0,'..')

from serve import test_method

class TestServer(unittest.TestCase):
  def test_flask_server(self):
    pass
    

test_method()
