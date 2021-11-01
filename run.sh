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

export RERE_PORT=$PORT # check if this works later

# required on linux
if  [ "`stat -c '%a' $PORT`" == "660" ] ; then
  echo changing permissions of $PORT to 660
  sudo chmod a+rw $PORT
fi

WRITE=1 ./db.py & 
pid=$!
./serve.py 
