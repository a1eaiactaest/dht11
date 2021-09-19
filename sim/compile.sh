#!/bin/bash -v

# make changes in .ino file, run this
# it takes some time to complete

arduino-cli upload -b arduino:avr:uno -p /dev/ttyACM0 -v
