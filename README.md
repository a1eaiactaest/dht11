# RERE

---

## Cloning

```sh
git clone https://github.com/a1eaiactaest/rere

cd rere/

git submodule update --init
```

Then run:

```sh
pip install -r requirements.txt
```

to satisfy python dependencies.

## Usage

### Local:

Start backend server:

```
python3 api/app.py
```

Read more about [API](api/README.md)  
Then start node.js running frontend:

```
cd frontend/ && npm start
```

### Docker:

Build and compose docker images:

```
docker-compose build -d
```

To stop them:

```
docker-compose stop
```

To remove:

```
docker-compose down
```

Now you can browse to `http://localhost:5000` to open the website.
