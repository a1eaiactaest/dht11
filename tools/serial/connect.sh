#!/bin/bash 

PORT=$(./find_port.sh)
if ls $PORT 2> /dev/null; then
  sudo screen $PORT 9600
fi

# this executes after deattaching from a screen session.
for scr in $(sudo screen -ls | awk '{print $1}'); do 
  sudo screen -S $scr -X kill; 
done
