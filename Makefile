build:
	@docker-compose build
	@make dep

dep:
	@docker-compose run discounts make dep

start:
	@docker-compose up -d

test:
	@docker-compose run discounts make test

compile-proto:
	@docker-compose run discounts make compile-proto
	@docker-compose run products make compile-proto
    