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
./connection.py /dev/ttyACM0
```
