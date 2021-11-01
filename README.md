# rere-api
-------------------------------------------------------------

<img src='docs/frog.jpg'>

<a href="http://forthebadge.com/"><img src="https://forthebadge.com/images/badges/built-with-swag.svg"></a>

## Usage

Find out what port master ((rx) with feather m0) station is on.
```
./tools/find_port.sh
```
It should return `/dev/tty*` on linux nad `/dev/tty.usb*` on mac.

Run `run.sh` script and pass port path as an argument. 
This will start `db.py` to write a line from serial to database every `n` seconds and a flask server to serve a website that displays database contents and plots dynamically.

```
./run.sh PORT
```

Browse to `localhost:5000`.

## Goals

* ~~every station has it's own table.~~ 
* dashboard (plots etc.)
* cleaner db and connection. 
* unit tests
* ~~interprate config.py from environment variables in db and serve~~
