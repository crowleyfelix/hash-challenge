build:
	@docker-compose build

start:
	@docker-compose up -d

compile-proto:
	@docker-compose run make compile-proto
    