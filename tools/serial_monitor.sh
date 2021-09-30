#!/bin/bash -e

PORT=readlink -f /dev/serial/by-id/*
if ls $PORT 2> /dev/null; then
  sudo screen $PORT 9600
fi
