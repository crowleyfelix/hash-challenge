package infrastructure

import (
	"fmt"
	"log"
	"net"

	"google.golang.org/grpc"
)

func ServeGRPC(register func(*grpc.Server)) {
	lis, err := net.Listen("tcp", fmt.Sprintf("%s:%s", Config.GRPCServer.Host, Config.GRPCServer.Port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	srv := grpc.NewServer()
	register(srv)

	log.Print("starting grpc server")
	if err := srv.Serve(lis); err != nil {
		log.Fatalf("failed to start server: %v", err)
	}
}
