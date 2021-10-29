# rere-api
-------------------------------------------------------------

## Usage

Setup your preferences in `config.py` directly.
Or pass right arugments in `db.py` and `connection.py` when calling the `Configuration` class.

Then run the startup shell script:
```
./run.sh PORT
```

## Goals

* ~~every station has it's own table.~~ 
* dashboard (plots etc.)
* cleaner db and connection. 
* unit tests
* interprate config.py from environment variables in db and serve
