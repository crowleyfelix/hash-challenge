package services

import (
	"context"
	"discounts/internal/domain"
	"discounts/internal/repositories"
	"discounts/proto"
	"log"
)

type discountCalculator struct {
	proto.UnimplementedDiscountCalculatorServer
}

func NewDiscountCalculator() *discountCalculator {
	return new(discountCalculator)
}

func (d *discountCalculator) Calculate(ctx context.Context, in *proto.CalculateRequest) (*proto.CalculateResponse, error) {
	log.Printf("received calculate discount request")
	prepo := repositories.NewProduct()
	urepo := repositories.NewUser()

	var (
		p   *domain.Product
		u   *domain.User
		err error
	)

	if p, err = prepo.Find(in.ProductId); err != nil {
		log.Printf("failed findind product %s", in.ProductId)
		return nil, err
	}

	if u, err = urepo.Find(in.UserId); err != nil {
		log.Printf("failed findind user %s", in.UserId)
		return nil, err
	}

	p.AddCalculators(domain.NewDiscountCalculators(u)...)

	return &proto.CalculateResponse{
		Product: (&product{p}).To(),
		User:    (&user{u}).To(),
	}, nil
}
