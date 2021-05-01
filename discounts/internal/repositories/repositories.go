package repositories

import (
	"discounts/internal/models"
	"discounts/internal/repositories/mongodb"
)

type ProductRepository interface {
	Find(string) (*models.Product, error)
}

type UserRepository interface {
	Find(string) (*models.User, error)
}

func NewProduct() ProductRepository {
	return new(mongodb.ProductRepository)
}

func NewUser() UserRepository {
	return new(mongodb.UserRepository)
}
