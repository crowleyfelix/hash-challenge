package services

import (
	"discounts/internal/domain"
	"discounts/proto"
)

type discount struct {
	*domain.Discount
}

func (d *discount) To() *proto.Discount {
	return &proto.Discount{
		Percentage:   d.Percentage,
		ValueInCents: d.ValueInCents,
	}
}

type product struct {
	*domain.Product
}

func (p *product) To() *proto.Product {
	d := discount{p.Discount()}
	var disc *proto.Discount

	if d.Discount != nil {
		disc = d.To()
	}

	return &proto.Product{
		Id:           p.ID,
		PriceInCents: p.PriceInCents,
		Title:        p.Title,
		Description:  p.Description,
		Discount:     disc,
	}
}

type user struct {
	*domain.User
}

func (u *user) To() *proto.User {
	return &proto.User{
		Id:        u.ID,
		FirstName: u.FirstName,
		LastName:  u.LastName,
	}
}
