package repositories

import (
	"discounts/internal/domain"
	"discounts/internal/repositories/mongodb"
)

type ProductRepository interface {
	Find(string) (*domain.Product, error)
}

type UserRepository interface {
	Find(string) (*domain.User, error)
}

func NewProduct() ProductRepository {
	return new(mongodb.ProductRepository)
}

func NewUser() UserRepository {
	return new(mongodb.UserRepository)
}
