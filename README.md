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
pip install -r requirements.txt 
```

to satisfy python dependencies.



## Usage

Find out what port master ((rx) with feather m0) station is on.
```
tools/serial/find_port.sh
```
It should return `/dev/tty*` on linux and `/dev/tty.usb*` on mac.

**TDB**

## TODO
 
1. write serial port data grabber
2. write data to the database
3. grab and post data to the website using tables, later charts (REACT)
4. improve website structure - edu, public api, site per station.
