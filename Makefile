VENV = env
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.ONESHELL:
create-dev-env:	requirements.txt
	docker pull postgres
	docker start postgresCont  > /dev/null 2>&1 || docker run -d --name postgresCont -p 5432:5432 -e POSTGRES_PASSWORD=pass123 -e POSTGRES_DB=djangotest postgres
	docker network inspect elastic > /dev/null 2>&1 || docker network create elastic
	docker pull docker.elastic.co/elasticsearch/elasticsearch:8.12.0
	docker start elasticcontainer > /dev/null 2>&1 || docker run -d --net elastic -p 9200:9200 --name elasticcontainer -e "ELASTIC_PASSWORD=localDev!123" docker.elastic.co/elasticsearch/elasticsearch:8.12.0
	sleep 20
	docker cp elasticcontainer:/usr/share/elasticsearch/config/certs/http_ca.crt .
	brew install postgresql@14
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	(docker ps -a | grep 'postgresCont' && docker rm -f postgresCont) > /dev/null 2>&1 || echo "postgresCont does not exist"
	(docker ps -a | grep 'elasticcontainer' && docker rm -f elasticcontainer) > /dev/null 2>&1 || echo "elasticcontainer does not exist"

run:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate
	yes | $(PYTHON) manage.py search_index --rebuild
	$(PYTHON) manage.py runserver

test:
	$(PYTHON) manage.py test