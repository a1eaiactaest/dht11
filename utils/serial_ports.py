import os
import platform

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

if __name__ == "__main__":
  print(find_serial_port())
