package main

import (
	"discounts/internal/infrastructure"
	"discounts/internal/repositories/mongodb"
	"log"
)

func main() {
	infrastructure.SetUpDB()
	log.Print("inserting fixtures")
	mongodb.ProductFixtures()
	mongodb.UserFixtures()
}
