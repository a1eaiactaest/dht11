import os
from random import randrange, choice 
import platform
from shutil import which
import atexit
import signal
import serial
import pty

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
  station = choice([3,5,11])
  pres = randrange(900, 1000)
  gas_res = randrange(0,255)
  a_temp = randrange(15,25)
  a_hum = randrange(40,60)
  gd_temp = randrange(0,10)
  gd_hum = randrange(60,100)

  return ' '.join(list(map(str, [station, pres, gas_res, a_temp, a_hum, gd_temp, gd_hum])))

class ArtificialSerial:
  """
  This creates a pseudo-terminal with serial port open.
  See https://en.wikipedia.org/wiki/Pseudoterminal
  Created terminal won't be visible for `find_serial_port` function above.

  Creates two file descriptors (master, slave). They are for reading and wrting data, respectively.

  Names of master and slavee are `/dev/pty{x_i}{y_i}` for i in x and y, 

  x: 'pqrstuvwxyzPQRST'
  y: '0123456789abcdef'

  """

  def __init__(self):
    self.master_fd, self.slave_fd = pty.openpty()
    self.slave_name = os.ttyname(self.slave_fd)
    self.ser = serial.Serial(self.slave_name)

    #print(f'Write to {self.slave_name}')

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
    self.ser.write(bytes(line, 'utf-8'))

  def close_pty(self, master_fd, slave_fd):
    os.close(master_fd)
    os.close(slave_fd)
    
  #@atexit.register
  def cleanup(self):
    """
    This is a trap for termnation signalls.
    When such a signal is recieved processes started by this class are killed and cleaned.
    Read: https://www.gnu.org/software/libc/manual/html_node/Termination-Signals.html
    """
    self.kill_process()
    signal.signal(signal.SIGTERM, self.kill_process)

if __name__ == "__main__":
  import time
  atty = ArtificialSerial()
  i = 0
  print(f"write to {atty.slave_name}")
  while (1):
    dummy_data = generate_dd()
    print('dummy: ', dummy_data)
    atty.write_line(dummy_data)
    print(os.read(atty.master_fd, 256).decode('utf-8'))
    time.sleep(1)
    
