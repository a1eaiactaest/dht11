#!/bin/bash -v

# python 

if ! ( dpkg -l | grep "Interactive high-level object-oriented language" &> /dev/null); then
  sudo apt install python3 python3-pip
fi

# pip deps

pip3 install pyserial flask  
  
