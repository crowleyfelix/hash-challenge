dep:
	@pipenv install -d

test:
	@pipenv run coverage run --source=app --branch -m unittest discover test -s .

compile-proto:
	@pipenv run python -m grpc_tools.protoc \
		-I /dist/proto \
		--python_out=./proto \
		--grpc_python_out=./proto \
		/dist/proto/discounts.proto