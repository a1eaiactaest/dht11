# rere-system
-------------------------------------------------------------

**This branch is a port from Flask to React.js.**

-------------------------------------------------------------

## Branches
Checkout the [react](https://github.com/a1eaiactaest/rere-system/tree/react) branch.

## Cloning
```sh
git clone https://github.com/a1eaiactaest/rere-system

cd rere-system/

git submodule update --init
```

Then run

```sh
./install.sh
```

to satisfy dependencies (mainly Python).

## Usage

Find out what port master ((rx) with feather m0) station is on.
```
tools/find_port.sh
```
It should return `/dev/tty*` on linux and `/dev/tty.usb*` on mac.

Run `run.sh` script. 
This will start `db.py` to write a line from serial to database every `n` seconds and a flask server to serve a website that displays database contents and plots it dynamically.

```sh
./run.sh
```
or if you want to specify the port:
```sh
./run.sh YOUR_PORT
```

Browse to `http://localhost:5000`.

## TODO
 
1. write serial port data grabber
2. write data to the database
3. grab and post data to the website using tables, later charts (REACT)
4. improve website structure - edu, public api, site per station.
