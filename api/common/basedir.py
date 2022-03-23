import os

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../"))
DATABASES = BASEDIR + '/api/databases/'

if __name__ == "__main__":
  print(BASEDIR)
  print(DATABASES)
