#!/bin/bash


SERIAL=`ls -f /dev/tty.usb*`
if ls /dev/tty.usb* 1> /dev/null 2>&1; then
  echo $SERIAL
else 
  echo "no serial ports detected"
fi
