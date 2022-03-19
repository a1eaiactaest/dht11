#!/usr/bin/env python3
import os 
from random import randrange, choice 
import platform
from shutil import which
import serial
import pty
import threading
import time

#DEBUG = os.getenv("DEBUG") is not None

def find_serial_port():
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
    raise Exception("more than one serial port has been found")
  elif len(ports) == 1: 
    return ports[0]
  else:
    raise Exception("no serial ports has been found")

def generate_dd():
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

# TODO: Write doc strings
class ArtificialSerial:
  def __init__(self):
    self.master_fd, self.slave_fd = pty.openpty() # set file descriptors
    self.slave_name = os.ttyname(self.slave_fd) # fd's name
    self.ser = serial.Serial(self.slave_name) 

  def create_pty(self):
    """
    > Open a new pseudo-terminal pair, using os.openpty() if possible, or emulation code for generic Unix systems. 
    > Return a pair of file descriptors (master, slave), for the master and the slave end, respectively.

    From https://docs.python.org/3/library/pty.html


    Returns slave file descriptor and slave pty name.
    """
    master, slave = pty.openpty()
    return master, slave

  def write_line(self, line):
    self.ser.write(line.encode())
    self.ser.reset_output_buffer()

  def close_pty(self, master_fd, slave_fd):
    os.close(master_fd)
    os.close(slave_fd)
    

class ASeriald:
  """
  artificial serial port daemon
  """
  def __init__(self):
    thread = threading.Thread(target=self.serial_daemon)
    thread.start()
    time.sleep(.1) # wait for thread to setup

  def serial_daemon(self):
    atty = ArtificialSerial()

    # that's how we get fd later, when we wan't to read from pseudo serial
    os.environ["RERE_FD"] = str(atty.master_fd) 

    # write dummy data every second
    while True:
      dd = generate_dd() # dummy
      atty.write_line(dd)

      time.sleep(1)

  def read(self, buf=32):
    return os.read(int(os.getenv("RERE_FD")), buf).decode("utf-8")

  def reset_output_buffer(self):
    pass

class Serial:
  """
  connect to phisical serial port and scrape data
  
  -- example data samples:
    -- normal

      "103 1009.00 120.00 20.00 52.00 2.00 87.00\n"

      
    -- error message
  """
  def __init__(self, port_name=None, baud=9600):
    if os.getenv("PORT", None) is None:
      if port_name is None:
        port_name = find_serial_port()     
    else:
      port_name = os.getenv("PORT")

    self.port_name = port_name
    self.baud = baud
    self.connection = self.connect()

    

  def connect(self):
    connection  = serial.Serial(self.port_name, self.baud) 
    connection.reset_input_buffer()

    return connection

  def integrity_check(self):
    assert self.port_name == self.connection.name, "var:port_name and var:connection.name are mismatched"

if __name__ == "__main__":
  S = Serial()
  #s = Seriald()
  #print(generate_dd())
  #print(find_serial_port())
  """
  while True:
    data_recv = s.read()
    # how many bytes message is, message it self
    print("%d: %s"%(len(bytes(data_recv, 'utf-8')), data_recv))
    time.sleep(2)
  """
