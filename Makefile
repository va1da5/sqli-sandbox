.PHONY: help restart


help:
	@echo "List of available commands:"
	@echo "restart                     - Restarts server container (including environment variables)"
	@echo "build                       - Builds web server container image"

restart:
	docker-compose rm -sf api
	docker-compose up -d api

build:
	docker-compose build