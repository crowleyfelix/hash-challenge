import os
import json
import bson
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import Collection
from app.repositories.mongodb import schemas
from app.infrastructure import ioc

FIXTURES_PATH = "/testdata"


class FixturesTask:
    def __init__(self):
        self.products = []
        self.users = []

    async def execute(self, params=None):
        config = ioc.instance(ioc.Dependencies.config)
        client = ioc.instance(ioc.Dependencies.mongodb_driver)
        self.db = client[config.mongodb.database]

        with open(f"{FIXTURES_PATH}/products.json") as f:
            documents = json.load(f)

            for document in documents:
                product = schemas.PRODUCT_SCHEMA.load(document)
                await self.db.products.insert_one(document)
                product["id"] = str(document.pop("_id"))
                self.products.append(product)

        with open(f"{FIXTURES_PATH}/users.json") as f:
            documents = json.load(f)
            documents[1]["dateOfBirth"] = datetime.now().isoformat()

            for document in documents:
                document["dateOfBirth"] = datetime.fromisoformat(document["dateOfBirth"])
                user = schemas.USER_SCHEMA.load(document)
                await self.db.users.insert_one(document)
                user["id"] = str(document.pop("_id"))
                self.users.append(user)

    async def revert(self):
        for product in self.products:
            await self.db.products.delete_one({"_id": bson.ObjectId(product["id"])})

        for user in self.users:
            await self.db.users.delete_one({"_id": bson.ObjectId(user["id"])})
