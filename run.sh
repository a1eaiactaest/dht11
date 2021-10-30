#!/bin/bash -e

function ctrl_c() {
  echo "*** stopping all started jobs ***"
  kill $pid
  exit 
}

trap ctrl_c 2 # 2 for SIGINT

if [ -z "$1" ]; then
  PORT="/dev/ttyACM0" # set your default port here
else
  PORT=$1
fi
  

if [ -z "$PORT" ]; then
  echo "please supply device port as argument"
  exit
fi

if  [ "`stat -c '%a' $PORT`" == "660" ] ; then
  echo changing permissions of $PORT to 660
  sudo chmod a+rw $PORT
fi
  
if [[ -n $2 ]] && [[ $2 == "SIM" ]]; then
  SIM=1 WRITE=1 ./db.py & 
  pid=$!
  SIM=1 ./serve.py 
else
  WRITE=1 ./db.py & 
  pid=$!
  ./serve.py 
fi
