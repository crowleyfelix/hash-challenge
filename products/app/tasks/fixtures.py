import os
import json
import bson
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import Collection
from app.repositories.mongodb import schemas
from app.infrastructure import ioc

FIXTURES_PATH = "/testdata"

class FixturesTask:
    def __init__(self):
        self.products = []

    async def execute(self, params=None):
        config = ioc.instance(ioc.Dependencies.config)
        client = ioc.instance(ioc.Dependencies.mongodb_driver)
        self.db = client[config.mongodb.database]

        with open(f"{FIXTURES_PATH}/products.json") as f:
            for document in json.load(f):
                product = schemas.PRODUCT_SCHEMA.load(document)
                await self.db.products.insert_one(document)
                product["id"] = str(document.pop("_id"))
                self.products.append(product)

    async def revert(self):
        for product in self.products:
            await self.db.products.delete_one({"_id": bson.ObjectId(product["id"])})


