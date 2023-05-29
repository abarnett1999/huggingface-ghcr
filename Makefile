# install: 
# 	pip install --upgrade pip &&\
# 		pip install -r requirements.txt

.PHONY: install run lint format test

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

run:
	uvicorn main:app --host 0.0.0.0 --port 8000

lint:
	flake8 --ignore=E501 .

format:
	black .

test:
	pytest

