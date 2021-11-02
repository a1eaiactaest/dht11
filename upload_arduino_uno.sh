#!/bin/bash -e

# make changes in .ino file, run this
# it takes some time to complete

# may come in handy
# https://arduino.github.io/arduino-cli/0.19/getting-started/

arduino-cli core install arduino:avr

sketch=$1
port=$2

arduino-cli compile --fqbn arduino:avr:uno $sketch
arduino-cli upload -p $port --fqbn arduino:avr:uno $sketch
