package domain

import (
	"discounts/internal/utils"
)

const (
	birthdayDiscountPerc    = 0.05
	blackFridayDiscountPerc = 0.1
	maxDiscountPerc         = 0.1
)

type Discount struct {
	Percentage   float64
	ValueInCents int64
}

type DiscountCalculator interface {
	Calculate(price int64) *Discount
}

func NewDiscountCalculators(user *User) []DiscountCalculator {
	return []DiscountCalculator{
		&birthdayDiscountRule{user},
		&blackFridayDiscountRule{},
	}
}

type birthdayDiscountRule struct{ user *User }

func (c *birthdayDiscountRule) Calculate(price int64) *Discount {

	//TODO: resolver time zone
	if _, month, day := utils.Now().Date(); month == c.user.DateOfBirth.UTC().Month() && day == c.user.DateOfBirth.UTC().Day() {
		return &Discount{
			Percentage:   birthdayDiscountPerc,
			ValueInCents: price - int64(float64(price)*birthdayDiscountPerc),
		}
	}

	return nil
}

type blackFridayDiscountRule struct{}

func (c *blackFridayDiscountRule) Calculate(price int64) *Discount {

	if _, month, day := utils.Now().Date(); month == 11 && day == 25 {
		return &Discount{
			Percentage:   blackFridayDiscountPerc,
			ValueInCents: int64(float64(price) * blackFridayDiscountPerc),
		}
	}

	return nil
}

type maxDiscountRule struct{}

func (c *maxDiscountRule) Calculate(price int64) *Discount {

	return &Discount{
		Percentage:   maxDiscountPerc,
		ValueInCents: int64(float64(price) * maxDiscountPerc),
	}
}
