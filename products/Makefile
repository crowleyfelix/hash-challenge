dep:
	@pipenv install -d

test:
	@nosetests tests

compile-proto:
	@pipenv run python -m grpc_tools.protoc -IPATH ./proto/discounts.proto --python_out=.