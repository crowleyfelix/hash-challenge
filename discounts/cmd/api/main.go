package main

import (
	"discounts/internal/services"
	"discounts/proto"
	"flag"
	"fmt"
	"log"
	"net"

	"google.golang.org/grpc"
)

func main() {
	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf("localhost:%s", "3000"))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	grpcServer := grpc.NewServer()
	proto.RegisterDiscountCalculatorServer(grpcServer, services.NewDiscountCalculator())

	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("failed to start server: %v", err)
	}
}
