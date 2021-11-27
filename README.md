# rere-api
-------------------------------------------------------------

<img src='docs/frog.jpg'>

<a href="http://forthebadge.com/"><img src="https://forthebadge.com/images/badges/built-with-swag.svg"></a>

There's a gene called [RERE](https://en.wikipedia.org/wiki/RERE)

## Usage

Find out what port master ((rx) with feather m0) station is on.
```
tools/find_port.sh
```
It should return `/dev/tty*` on linux nad `/dev/tty.usb*` on mac.

Run `run.sh` script. 
This will start `db.py` to write a line from serial to database every `n` seconds and a flask server to serve a website that displays database contents and plots dynamically.

```
./run.sh
```
or if you want to specify the port:
```
./run.sh YOUR_PORT
```

Browse to `http://localhost:5000`.

## Goals

* QA
* dashboard (plots etc.)
* [Issues](https://github.com/a1eaiactaest/rere-api/issues)

    


[Great song about RERE](https://www.youtube.com/watch?v=HAgdfTsCmSI)
