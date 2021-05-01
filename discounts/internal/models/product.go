package models

type Product struct {
	ID           string
	PriceInCents int64
	Title        string
	Description  string
	Discount     *ProductDiscount
}

type ProductDiscount struct {
	Percentage   float64
	ValueInCents int64
}
