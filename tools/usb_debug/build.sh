#!/bin/bash
g++ --std=c++11 -I /home/ufo/build/libusb-1.0.24/libusb main.cc -Wdeprecated-declarations
./a.out
