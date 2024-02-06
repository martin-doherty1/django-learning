VENV = env
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.ONESHELL:
create_dev_env:	requirements.txt
	brew install postgresql@14
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)