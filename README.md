# rere-api
-------------------------------------------------------------

## Running the simulator

There's no need to run separate python scripts now.

First, run the startup script and supply arduino port as the argument.
```
./run.sh /dev/ttyACM0
```

Then browse to `localhost:5000`.

## Connection


**!ALL OF THIS IS NOW COVERED IN STARTUP SCRIPT!**

Connect arduino via USB B. Find out which port arduino is on. Should be `/dev/tty*`, usually `ttyACM0` or `ttyUSB0`.  

In order to read serial port device needs proper privileges.

```bash
sudo chmod a+rw DEVICE
```

```
# check if serial connection works. make sure there aren't any other connections to the serial port.
./connection.py DEVICE
```

It should display the simulation values in stdout.

```
[1.0, 1000.3, 124.23, 24.34, 61.57, 15.12, 71.3, 69.42, 42.07, 45.65, 0.0]
```

