#!/bin/bash -v

# python 

if ! ( dpkg -l | grep "Interactive high-level object-oriented language" &> /dev/null); then
  sudo apt install python3 python3-pip
fi

# pip deps

pip3 install pyserial flask rethinkdb
  
# rethinkdb

source /etc/lsb-release 
echo "deb https://download.rethinkdb.com/repository/ubuntu-$DISTRIB_CODENAME $DISTRIB_CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list
wget -qO- https://download.rethinkdb.com/repository/raw/pubkey.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install rethinkdb


