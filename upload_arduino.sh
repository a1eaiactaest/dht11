#!/bin/bash -e

# make changes in .ino file, run this
# it takes some time to complete

arduino-cli compile --fqbn arduino:avr:uno $1
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno $1
