import os
import platform
from subprocess import Popen, check_call, STDOUT
from shutil import which
import atexit
import signal
import serial

def find_serial_port():
  """
  Search for serial port in /dev, works on Mac and Linux.
  Returns absolute path as a string.
  """
  devices = os.listdir("/dev")
  if platform.system() == "Darwin":
    ports = [f"/dev/{port}" for port in devices if "tty.usb" in port]
  elif platform.system() == "Linux":
    ports = [f"/dev/{port}" for port in devices if "ttyACM" or "ttyUSB" in port]

  if len(ports) > 1:
    print("more than one serial port has been found")
    return
  else: return ports[0]

class ArtificialSerial:
  """
  This creates a pseudo-terminal with serial port open.
  See https://en.wikipedia.org/wiki/Pseudoterminal
  Created terminal won't be visible for `find_serial_port` function above.

  Socat command creates two ports with symlinks to /tmp/ttyRERETX and /tmp/ttyRERERX
  """

  def __init__(self):
    self.create_pty()
    atexit.register(self.kill_process, self.socat_ptys_pid) # function, functions paramter
    signal.signal(signal.SIGTERM, self.kill_process)

  def create_pty(self):
    self.DEVNULL = open(os.devnull, "wb")
    # Run background socat
    if self.is_installed("socat"):
      # suppres socat output
      try:
        read_port = '/tmp/RERETX'
        write_port = '/tmp/RERERX'
        socat_ptys = Popen(f"socat -d -d pty,raw,echo=0,link={read_port} pty,raw,echo=0,link={write_port}".split(" "), 
                            stdout=self.DEVNULL, stderr=STDOUT)
        # save pid, kill later
        self.socat_ptys_pid = socat_ptys.pid
        print(f"pty's PID: {self.socat_ptys_pid}")
        print('read: ', read_port)
        print('write:', write_port)
      finally:
        self.DEVNULL.close()
    else:
      print("please install socat")
  
  def is_installed(self, programs_name):
    """
    Check whether given program is installed and added to $PATH
    """
    return which(programs_name) is not None

  def kill_process(self, pid=None):
    """
    Takes process PID as a paramter.
    Terminates program under PID with SIGKILL, SIGTERM can be handled.

    Note: The functions registered via this module are not called when 
    the program is killed by a signal not handled by Python, 
    when a Python fatal internal error is detected, or when os._exit() is called.

    https://docs.python.org/3/library/atexit.html#module-atexit
    """
    if not pid:
      pid = self.socat_ptys_pid
    os.kill(pid, signal.SIGKILL)
    print(f"SIGKILL {pid}")
  

if __name__ == "__main__":
  #print(find_serial_port())
  import time
  a = ArtificialSerial()
  i = 0
  #s = serial.Serial('/tmp/RERERX')
  while (1):
    #print(s.readline())
    pass

