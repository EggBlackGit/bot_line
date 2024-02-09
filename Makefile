.PHONY: start
start:
	python run.py

install:
	pip install -U -r requirements.txt


.PHONY: migrate
migrate:
	alembic upgrade head
