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
		&blackFridayDiscountRule{user},
	}
}

type birthdayDiscountRule struct{ user *User }

func (c *birthdayDiscountRule) Calculate(price int64) *Discount {
	bday := c.user.DateOfBirth
	now := utils.Now().In(bday.Location())

	//TODO: resolver time zone
	if _, month, day := now.Date(); month == bday.Month() && day == bday.Day() {
		return &Discount{
			Percentage:   birthdayDiscountPerc,
			ValueInCents: price - int64(float64(price)*birthdayDiscountPerc),
		}
	}

	return nil
}

type blackFridayDiscountRule struct{ user *User }

func (c *blackFridayDiscountRule) Calculate(price int64) *Discount {
	now := utils.Now().In(c.user.DateOfBirth.Location())

	if _, month, day := now.Date(); month == 11 && day == 25 {
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
