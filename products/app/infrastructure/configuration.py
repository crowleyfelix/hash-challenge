import os
from pydantic import BaseModel, BaseSettings, Field


class MongoDBConfig(BaseSettings):
    uri: str = Field(env="MONGODB_URI")
    database: str = Field(env="MONGODB_DATABASE")


class ApplicationConfig(BaseSettings):
    mongodb: MongoDBConfig = MongoDBConfig()
    port: int = Field(default=8081, env="PORT")
    fixtures_path: str = Field(default="/testdata", env="FIXTURES_PATH")
