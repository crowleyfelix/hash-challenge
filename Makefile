build:
	@cp discounts/.env.example discounts/.env
	@cp products/.env.example products/.env
	@docker-compose build
	@make start fixtures test

dep:
	@docker-compose run products make dep

start:
	@docker-compose up -d

stop:
	@docker-compose down

fixtures:
	@docker-compose run discounts make fixtures

test:
	@docker-compose run discounts make test
	@docker-compose run products make test

compile-proto:
	@docker-compose run discounts make compile-proto
	@docker-compose run products make compile-proto
    