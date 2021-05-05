package main

import (
	"discounts/internal/infrastructure"
	"discounts/internal/services"
	"discounts/proto"
	"log"

	"google.golang.org/grpc"
)

func main() {
	infrastructure.SetUpDB()
	infrastructure.ServeGRPC(func(sv *grpc.Server) {
		log.Printf("registering grpc services")
		proto.RegisterDiscountCalculatorServer(sv, services.NewDiscountCalculator())
	})
}
