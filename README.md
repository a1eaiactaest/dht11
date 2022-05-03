# RERE
-------------------------------------------------------------

## Cloning
```sh
git clone https://github.com/a1eaiactaest/rere

cd rere/

git submodule update --init
```

Then run

```sh
pip install -r requirements.txt 
```

to satisfy python dependencies.


## Usage

Start backend server: 

```
python3 api/app.py
```
Read more about [API](api/README.md) 




Then start node.js running frontend:

```
cd frontend/ && npm start
```

Now you can browse to `http://localhost:5000` to open the website.
