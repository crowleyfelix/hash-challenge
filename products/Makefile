dep:
	@pipenv install -d

test:
	@nosetests tests

compile-proto:
	@pipenv run python -m grpc_tools.protoc -I ./proto --python_out=./proto ./proto/discounts.proto