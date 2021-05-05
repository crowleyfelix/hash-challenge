import os
import multiprocessing
from pydantic import BaseModel, BaseSettings, Field


class ServerConfig(BaseSettings):
    host: str = Field(default="0.0.0.0", env="SERVER_HOST")
    port: int = Field(default=8081, env="PORT")
    workers: int = Field(default=multiprocessing.cpu_count() * 2 + 1, env="SERVER_WORKERS")


class LogConfig(BaseSettings):
    access_level: str = Field(default="info", env="LOG_ACCESS_LEVEL")
    level: str = Field(default="info", env="LOG_LEVEL")


class MongoDBConfig(BaseSettings):
    uri: str = Field(env="MONGODB_URI")
    database: str = Field(env="MONGODB_DATABASE")


class DiscountsApiConfig(BaseSettings):
    host: str = Field(default="discounts", env="DISCOUNTS_API_HOST")
    port: int = Field(default=80, env="DISCOUNTS_API_PORT")


class ApplicationConfig(BaseSettings):
    name: str = "products-api"
    server: ServerConfig = ServerConfig()
    log: LogConfig = LogConfig()
    mongodb: MongoDBConfig = MongoDBConfig()
    discounts_api: DiscountsApiConfig = DiscountsApiConfig()
    fixtures_path: str = Field(default="/testdata", env="FIXTURES_PATH")
