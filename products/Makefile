dep:
	@pipenv install -d

start:
	@pipenv run python -m app.tasks.server

test:
	@pipenv run coverage run --source=app --branch -m unittest discover test -s .
	@pipenv run coverage report --include=$(shell pwd)/* --ignore-errors

compile-proto:
	@pipenv run python -m grpc_tools.protoc \
		-I /dist/proto \
		--python_out=./proto \
		--grpc_python_out=./proto \
		/dist/proto/discounts.proto