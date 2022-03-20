#!/bin/bash -e

# make changes in .ino file, run this
# it takes some time to complete

# may come in handy
# https://arduino.github.io/arduino-cli/0.19/getting-started/

# Example:
# ./upload_arduino_uno.sh dummy /dev/tty.usbserial-A50285BI 

arduino-cli core install arduino:avr

sketch=$1
port=$(serial/find_port.sh)

echo $port

arduino-cli compile --fqbn arduino:avr:uno $sketch
arduino-cli upload -p $port --fqbn arduino:avr:uno $sketch
