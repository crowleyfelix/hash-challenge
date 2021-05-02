package mongodb

import (
	"discounts/internal/domain"

	"github.com/kamva/mgm/v3"
)

type repository struct{}

func (repo *repository) Find(id string, model mgm.Model) error {
	coll := mgm.Coll(model)

	if err := coll.FindByID(id, model); err != nil {
		return err
	}

	return nil
}

type ProductRepository struct{ repository }

func (repo *ProductRepository) Find(id string) (*domain.Product, error) {
	data := new(Product)
	if err := repo.repository.Find(id, data); err != nil {
		return nil, err
	}

	return &domain.Product{
		ID:           data.ID.Hex(),
		Title:        data.Title,
		Description:  data.Description,
		PriceInCents: data.PriceInCents,
	}, nil
}

type UserRepository struct{ repository }

func (repo *UserRepository) Find(id string) (*domain.User, error) {
	data := new(User)
	if err := repo.repository.Find(id, data); err != nil {
		return nil, err
	}

	return &domain.User{
		ID:          data.ID.Hex(),
		FirstName:   data.FirstName,
		LastName:    data.LastName,
		DateOfBirth: data.DateOfBirth,
	}, nil
}
