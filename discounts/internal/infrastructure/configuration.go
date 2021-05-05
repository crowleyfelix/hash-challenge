package infrastructure

type mongoDBConfig struct {
	URI      string `env:"MONGODB_URI" env-default:"mongodb://mongodb:27017"`
	Database string `env:"MONGODB_DATABASE" env-default:"hash"`
}

type grpcServerConfig struct {
	Host string `env:"GRPC_HOST" env-default:"0.0.0.0"`
	Port string `env:"GRPC_PORT" env-default:"80"`
}

type appConfig struct {
	FixturesPath string `env:"FIXTURES_PATH" env-default:"/go/testdata"`
	GRPCServer   grpcServerConfig
	MongoDB      mongoDBConfig
}
