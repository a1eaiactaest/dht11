#!/bin/bash -e

function ctrl_c() {
  echo "*** stopping all started jobs ***"
  kill $pid
  exit 
}

trap ctrl_c 2 # 2 for SIGINT

#PORT=$(readlink -f /dev/serial/by-id/*) # this wont work for mac
PORT=$1

if [ -z "$PORT" ]; then
  echo "please supply device port as argument"
  exit
fi

if  [ "`stat -c '%a' $PORT`" == "660" ] ; then
  echo changing permissions of $PORT to 660
  sudo chmod a+rw $PORT
fi
  
if [[ -n $1 ]] && [[ $1 == "SIM" ]]; then
  SIM=1 WRITE=1 ./db.py & 
  pid=$!
  SIM=1 ./serve.py 
else
  WRITE=1 ./db.py & 
  pid=$!
  ./serve.py 
fi
