Serial tools
-----

Made for better experience.

## tmux_monitor

```
./tmux_monitor.sh
```

Launches the tmux session with tools needed to monitor the performace of the Flask server and database writer.

It's worth remembering that exiting tmux session won't kill it. It is still running in the background. 

Run this script again to attach back to it.

In order to kill the tmux session detach and do:
```
./tmux_monitor.sh kill
```

If not familiar with tmux read [man pages](https://man7.org/linux/man-pages/man1/tmux.1.html).


# find_port

Don't know what serial port master station is on?

```
./find_port.sh
```

Should return you `/dev/tty.usb*` on Macs and  
`/dev/tty*` on linux.


# serial_monitor

Want to see whats sent to specific serial port?

```
./serial_monitor.sh
```

This will make screen session with serial outputs on it.


