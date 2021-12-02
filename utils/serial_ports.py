import os
import platform
from subprocess import Popen, check_call, STDOUT
from shutil import which
import atexit
import signal

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

class VirtualSerial:
  """
  This creates a pseudo-terminal with serial port open.
  See https://en.wikipedia.org/wiki/Pseudoterminal
  Created terminal won't be visible for `find_serial_port` function above.

  Socat command creates two ports with symlinks to /tmp/ttyRERETX and /tmp/ttyRERERX
  """

  def __init__(self):
    self.create_pty()
    atexit.register(self.kill_process, self.socat_ptys_pid) # function, functions paramter

  def create_pty(self):
    self.DEVNULL = open(os.devnull, "wb")
    # Run background socat
    if self.is_installed("socat"):
      # suppres socat output
      try:
        socat_ptys = Popen("socat -d -d pty,raw,echo=0,link=/tmp/ttyRERETX pty,raw,echo=0,link=/tmp/ttyRERERX".split(" "), 
                            stdout=self.DEVNULL, stderr=STDOUT)
        # save pid, kill later
        self.socat_ptys_pid = socat_ptys.pid
        print(f"pty's PID: {self.socat_ptys_pid}")
      finally:
        self.DEVNULL.close()
    else:
      print("please install socat")
  
  def is_installed(self, programs_name):
    """
    Check whether given program is installed and added to $PATH
    """
    return which(programs_name) is not None

  def kill_process(self, pid):
    """
    Takes process PID as a paramter.
    Terminates program under PID with SIGKILL, SIGTERM can be handled.

    Note: The functions registered via this module are not called when 
    the program is killed by a signal not handled by Python, 
    when a Python fatal internal error is detected, or when os._exit() is called.

    https://docs.python.org/3/library/atexit.html#module-atexit
    """
    os.kill(pid, signal.SIGKILL)
    print(f"SIGKILL {pid}")
  

if __name__ == "__main__":
  #print(find_serial_port())
  import time
  vs = VirtualSerial()
  while (1):
    time.sleep(10000)


