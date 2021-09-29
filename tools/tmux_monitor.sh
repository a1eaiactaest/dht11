#!/bin/bash

# check whether session already exists
tmux has-session -t rere-monitor 2>/dev/null
if [ $? != 0 ]; then
  tmux new -d -s rere-monitor

  # install htop if needed
  if ! command -v "htop" > /dev/null 2>&1; then
    sudo apt install htop
  fi

  tmux send-keys "htop" ENTER

  tmux neww
  tmux send-keys "./launch_client.sh" ENTER
fi

# attach to the session
tmux a -t rere-monitor
