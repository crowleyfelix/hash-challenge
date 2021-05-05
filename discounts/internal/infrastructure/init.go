package infrastructure

import (
	"log"

	"github.com/ilyakaznacheev/cleanenv"
	"github.com/kamva/mgm/v3"
	"go.mongodb.org/mongo-driver/mongo/options"
)

var Config appConfig

func init() {
	log.Println("loading configurations")
	if err := cleanenv.ReadEnv(&Config); err != nil {
		log.Fatalf(err.Error())
	}
}

func SetUpDB() {
	log.Println("connecting to mongodb")
	if err := mgm.SetDefaultConfig(nil, Config.MongoDB.Database, options.Client().ApplyURI(Config.MongoDB.URI)); err != nil {
		log.Fatalf("failed connecting with mongodb: %v", err)
	}
}
