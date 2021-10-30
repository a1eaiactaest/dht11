# rere-api
-------------------------------------------------------------

<img src='docs/frog.jpg'>

## Usage

Setup your preferences in `config.py` directly.
Or pass right arugments in `db.py` and `connection.py` when calling the `Configuration` class.

Then run the startup shell script:
```
./run.sh PORT
```

browse to `localhost:5000`

## Goals

* ~~every station has it's own table.~~ 
* dashboard (plots etc.)
* cleaner db and connection. 
* unit tests
* interprate config.py from environment variables in db and serve
