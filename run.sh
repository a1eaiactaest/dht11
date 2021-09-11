#!/bin/bash -e

if [ -z "$1" ]; then
  echo please supply device as argument
  exit
fi

if  [ "`stat -c '%a' $1`" == "660" ] ; then
  echo changing permissions of $1 to crw-rw-rw-
  sudo chmod a+rw $1
fi
  

if  [ "`stat -c '%a' $1`" == "666" ] ; then
  echo permissions of $1 are right [666]
fi

python3 serve.py $1
