package errors

import (
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
)

func NewNotFound(id string) error {
	return grpc.Errorf(codes.NotFound, "resource with id %s was not found", id)
}
