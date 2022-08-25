.PHONY: help setup setup-info setup-down produce install uninstall reinstall
.DEFAULT: help

help:
	@echo "make setup"
	@echo "          Setup project"
	@echo "----------"
	@echo "make setup-info"
	@echo "          View infrastructure status"
	@echo "----------"
	@echo "make setup-down"
	@echo "          Removing the infrastructure"
	@echo "----------"
	@echo "make produce"
	@echo "          Produce data to Kafka topic"
	@echo "----------"
	@echo "make consume"
	@echo "          Consume data to Kafka topic"
	@echo "----------"
	@echo "make install"
	@echo "          Install packages"
	@echo "----------"
	@echo "make uninstall"
	@echo "          Uninstall packages"
	@echo "----------"
	@echo "make reinstall"
	@echo "          Reinstall packages"
	@echo "----------"

setup:
	@echo "Setting up the project ..."
	@echo "----------"
	docker-compose up -d

setup-info:
	@echo "View infrastructure status"
	@echo "----------"
	docker ps -a | grep -E 'kafka|zookeeper|kafdrop'

setup-down:
	@echo "Removing infrastructure ..."
	@echo "----------"
	docker-compose down

produce:
	poetry run produce

consume:
	poetry run consume

install:
	pip install poetry && poetry install

uninstall:
	poetry cache clear pypi --all && rm -f poetry.lock

reinstall: uninstall install