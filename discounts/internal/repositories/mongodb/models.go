package mongodb

import (
	"time"

	"github.com/kamva/mgm/v3"
)

type Product struct {
	mgm.DefaultModel `bson:",inline"`
	PriceInCents     int64  `bson:"priceInCents"`
	Title            string `bson:"Title"`
	Description      string `bson:"description"`
}

type User struct {
	mgm.DefaultModel `bson:",inline"`
	FirstName        string    `bson:"firstName"`
	LastName         string    `bson:"lastName"`
	DateOfBirth      time.Time `bson:"dateOfBirth"`
}
