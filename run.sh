#!/bin/bash -e

function ctrl_c() {
  echo "*** stopping all started jobs ***"
  kill $pid
  exit 
}

trap ctrl_c 2 # 2 for SIGINT

if [ -z "$1" ]; then
  echo "please supply reciever serial port as an argument"
  exit
else
  PORT=$1
fi

export PORT=$PORT # check if this works later

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
