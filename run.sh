#!/bin/bash -e

function ctrl_c() {
  echo "*** stopping all started jobs ***"
  kill $pid
  exit 
}

trap ctrl_c 2 # 2 for SIGINT

PORT=readlink -f /dev/serial/by-id/*

if [ -z "$PORT" ]; then
  echo "please supply device port as argument"
  exit
fi

if  [ "`stat -c '%a' $PORT`" == "660" ] ; then
  echo changing permissions of $PORT to 660
  sudo chmod a+rw $PORT
fi
  
WRITE=1 ./db.py & 
pid=$!
./serve.py 
