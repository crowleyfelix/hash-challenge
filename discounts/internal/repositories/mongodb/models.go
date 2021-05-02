package mongodb

import (
	"time"

	"github.com/kamva/mgm/v3"
)

type Product struct {
	mgm.DefaultModel `bson:",inline"`
	PriceInCents     int64  `json:"priceInCents" bson:"priceInCents"`
	Title            string `json:"title" bson:"title"`
	Description      string `json:"description" bson:"description"`
}

type User struct {
	mgm.DefaultModel `bson:",inline"`
	FirstName        string    `json:"firstName" bson:"firstName"`
	LastName         string    `json:"lastName" bson:"lastName"`
	DateOfBirth      time.Time `json:"dateOfBirth" bson:"dateOfBirth"`
}
