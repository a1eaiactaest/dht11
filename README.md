# rere-api
-------------------------------------------------------------

### Connection

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

### Website

Run the database handler in one terminal or the background. 

```
WRITE=1 ./db.py
```

Display data dynamically on the website.

```
./serve.py
```
