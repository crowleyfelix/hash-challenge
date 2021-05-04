package mongodb

import (
	"log"

	"github.com/kamva/mgm/v3"
	"go.mongodb.org/mongo-driver/mongo/options"
)

func init() {
	// Setup the mgm default config
	err := mgm.SetDefaultConfig(nil, "hash", options.Client().ApplyURI("mongodb://mongodb:27017"))

	if err != nil {
		log.Fatalf("failed connecting with mongodb: %v", err)
	}
}
