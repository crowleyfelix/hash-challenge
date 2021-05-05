package domain

import "log"

type Product struct {
	ID           string
	PriceInCents int64
	Title        string
	Description  string
	calcs        []DiscountCalculator
}

func (p *Product) AddCalculators(calcs ...DiscountCalculator) {
	for _, calc := range calcs {
		p.calcs = append(p.calcs, calc)
	}
}

func (p *Product) Discount() *Discount {
	log.Printf("calculating discounts")
	c := make(chan *Discount, len(p.calcs))

	for _, calc := range p.calcs {

		go func(calc DiscountCalculator, out chan *Discount) {
			out <- calc.Calculate(p.PriceInCents)
		}(calc, c)
	}

	disc := new(Discount)

	for i := 0; i < len(p.calcs); i++ {
		d := <-c

		if d == nil {
			continue
		}

		disc.Percentage = disc.Percentage + d.Percentage
		disc.ValueInCents = disc.ValueInCents + d.ValueInCents

		if disc.Percentage >= maxDiscountPerc {
			return new(maxDiscountRule).Calculate(p.PriceInCents)
		}
	}

	if disc.Percentage == 0 {
		log.Printf("no discount available")
		return nil
	}

	return disc
}
