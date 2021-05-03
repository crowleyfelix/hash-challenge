dep:
	@pipenv install -d

test:
	@nosetests tests

compile-proto:
	@pipenv run python -m grpc_tools.protoc \
		-I /dist/proto \
		--python_out=./proto \
		/dist/proto/discounts.proto