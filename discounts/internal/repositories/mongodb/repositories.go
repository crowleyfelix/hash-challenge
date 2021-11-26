package mongodb

import (
	"discounts/internal/domain"
	"discounts/internal/errors"
	"time"

	"github.com/kamva/mgm/v3"
	"go.mongodb.org/mongo-driver/mongo"
)

type repository struct{}

func (repo *repository) Find(id string, model mgm.Model) error {
	coll := mgm.Coll(model)

	if err := coll.FindByID(id, model); err != nil {
		if err == mongo.ErrNoDocuments {
			return errors.NewNotFound(id)
		}
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

	loc, _ := time.LoadLocation(data.Location)

	return &domain.User{
		ID:          data.ID.Hex(),
		FirstName:   data.FirstName,
		LastName:    data.LastName,
		DateOfBirth: data.DateOfBirth.In(loc),
		Location:    data.Location,
	}, nil
}
