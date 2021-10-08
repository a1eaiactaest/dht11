#!/bin/bash 

PORT=$(readlink -f /dev/serial/by-id/*)
if ls $PORT 2> /dev/null; then
  sudo screen $PORT 9600
fi

for scr in $(sudo screen -ls | awk '{print $1}'); do 
  sudo screen -S $scr -X kill; 
done
