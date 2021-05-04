import os
import json
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import Collection
from app.repositories.mongodb import schemas

FIXTURES_PATH = "/testdata"

class FixturesTask:
    def __init__(self):
        self.products = []
        self.client = AsyncIOMotorClient("mongodb://mongodb:27017",
                                     uuidRepresentation="standard",
                                     connect=False)
        self.db = self.client.mgm_lab

    async def execute(self, params=None):
        with open(f"{FIXTURES_PATH}/products.json") as f:
            for document in json.load(f):
                product = schemas.PRODUCT_SCHEMA.load(document)
                await self.db.products.insert_one(document)
                product["id"] = str(document.pop("_id"))
                self.products.append(product)

    async def revert(self):
        for product in self.products:
            await self.db.products.delete_one({"_id": product["id"]})


