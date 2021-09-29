#!/bin/bash

# find port, may be prone to bugs, will see
PORT=$(readlink -f /dev/serial/by-id/*)

(cd .. && ./run.sh $PORT)
