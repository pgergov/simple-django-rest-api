## To setup PostgreSQL

* Install prerequisites:

```bash
$ sudo apt-get update
$ sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib
```

* Create database & database user: 

```bash
$ sudo su - postgres
$ psql
postgres=# CREATE DATABASE "simple-django-rest-api";
postgres=# CREATE USER "demouser" WITH PASSWORD 'password';
postgres=# GRANT ALL PRIVILEGES ON DATABASE "simple-django-rest-api" to "demouser";
postgres=# \q
$ exit
```

## Install requirements

```bash
$ pip install -r requirements.txt
```

## Run migrations

```python
python manage.py migrate
```

## Run server

```python
python manage.py runserver
```

* Browse the goodies list api @ `http://localhost:8000/goods/list/`
