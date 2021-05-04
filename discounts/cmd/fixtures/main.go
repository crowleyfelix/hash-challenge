package main

import "discounts/internal/repositories/mongodb"

func main() {
	mongodb.ProductFixtures()
	mongodb.UserFixtures()
}
