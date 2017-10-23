# MySQL Proxy API

## Necessary Environment variables:

```
MYSQL_HOST
MYSQL_USER
MYSQL_PASSWORD
MYSQL_DATABASE
```

## Start the app:

```
source .env
FLASK_APP=app.py flask run
```

## Docker build:

```
docker build -t mysql-proxy-api:latest .
```

## Docker run:

```
docker run -p 5000:5000 --rm -it --env-file=.env mysql-proxy-api:latest
```

## Test the app:

```
curl -i -H "Content-Type: application/json" -X POST -d '{"query":"select * from something"}'  0.0.0.0:5000/query
```
