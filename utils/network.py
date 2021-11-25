import re
import requests
from db import Database

def init_db():
  db = Database()
  return db

def url_is_up(url, title):
  try:
    src_code = str(requests.get(url).content)
    if re.search(f'<title>{title}', src_code):
      return True
    return False
  except requests.exceptions.ConnectionError:
    # Couldn't resolve connection
    return False

if __name__ == "__main__":
  print(url_is_up("http://localhost:5000/", "RERE"))
