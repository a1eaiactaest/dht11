#!/bin/bash -e

#set -m 

function ctrl_c() {
  echo "*** stopping all started jobs ***"
  kill $pid
  exit 
}

trap ctrl_c 2 # 2 for SIGINT

if [ -z "$1" ]; then
  echo "please supply device as argument"
  exit
fi

if  [ "`stat -c '%a' $1`" == "660" ] ; then
  echo changing permissions of $1 to 660
  sudo chmod a+rw $1
fi
  
WRITE=1 ./db.py & 
pid=$!
#echo "$pid"
./serve.py 
