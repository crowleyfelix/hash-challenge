package main

import (
	"discounts/internal/infrastructure"
	"discounts/internal/repositories/mongodb"
	"log"
)

func main() {
	infrastructure.SetUpDB()
	log.Print("inserting fixtures")

	users, _ := mongodb.UserFixtures()
	for _, us := range users {
		log.Printf("user{id:%s name:%s dateOfBirth:%s}", us.ID.Hex(), us.FirstName, us.DateOfBirth)
	}

	products, _ := mongodb.ProductFixtures()
	for _, pr := range products {
		log.Printf("product{id:%s title:%s}", pr.ID.Hex(), pr.Title)
	}
}
