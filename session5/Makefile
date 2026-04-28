.PHONY: up down build install

up:
	docker compose -f dockercompose.yaml up --build

down:
	docker compose -f dockercompose.yaml down --remove-orphans

build:
	docker compose -f dockercompose.yaml build

install:
	uv pip install -r requirements.txt
