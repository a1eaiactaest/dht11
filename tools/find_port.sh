#!/bin/bash

if [ `uname` == "Darwin" ]; then
  SERIAL=`ls -f /dev/tty.usb*`
  if ls /dev/tty.usb* 1> /dev/null 2>&1; then
    echo $SERIAL
  else 
    echo "no serial ports detected"
  fi
elif [ `uname` == "Linux" ]; then
  SERIAL=`readlink /dev/serial/by-id/*`
  echo $SERIAL
fi
