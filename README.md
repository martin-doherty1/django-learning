## Django Elastic Learning

# To create postgres docker container
``docker run -d --name postgresDB -p 5432:5432 -e POSTGRES_PASSWORD=pass123 postgres``

### [To create local instance of elastic search](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)

#### Django Commands

To make migrations for DB:
    ``python3 manage.py makemigrations [app-name]``

To run migrations for DB:
    ``python3 manage.py migrate``

To create superuser for django admin:
    ``python3 manage.py createsuperuser``

To run tests:
    ``python3 manage.py test [app-name]``

To create django app:
    ``python3 manage.py startapp [app-name]``

To rebuild elastic indices:
    ``python3 manage.py search_index --rebuild``

#### To create local development environment

Create python virtual environment:
    ``python3 -m venv <environment-name>``

To activate virtual environment:
    ``source <environment-name>/bin/activate``

To install development requirements:
    ``pip install -r requirements.txt``

