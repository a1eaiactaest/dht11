#!/bin/bash 

function ctrl_c() {
  echo "*** stopping all started jobs ***"
  kill $db_pid
  exit 
}

trap ctrl_c 2 # 2 for SIGINT

if [ -z "$1" ]; then
  echo "searching for open serial port..."
  PORT=`./tools/find_port.sh`
  FIND_PORT_RETURNCO=$?
  if [ $FIND_PORT_RETURNCO -ne 0 ]; then
    echo "port couldn't be found"
    read -p "do you want to create artificial serial port? type [yes/no]: " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then 
      echo "creating the artificial serial port..."
      # execute python serial port class here
      echo "NotImplementedYetError"
      exit 1
    fi
  fi
  echo "port found -> $PORT"
  exit 1
else
  PORT=$1
fi

export RERE_PORT=$PORT # check if this works later

# required on linux
if [ `uname` == "Linux" ]; then
  if  [ "`stat -c '%a' $PORT`" == "660" ] ; then
    echo changing permissions of $PORT to 660
    sudo chmod a+rw $PORT
  fi
fi

echo "starting db.py in WRITE mode"
WRITE=1 ./db.py & 
db_pid=$!
echo "starting flask server"
./serve.py 

