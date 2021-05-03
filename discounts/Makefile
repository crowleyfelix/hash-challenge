dep:
	@go mod vendor

test:
	@ginkgo -cover ./...

fixtures:
	@go run cmd/fixtures/main.go

compile-proto:
	@protoc --go_out=. --go_opt=paths=source_relative \
		--go-grpc_out=. --go-grpc_opt=paths=source_relative \
		proto/discounts.proto
