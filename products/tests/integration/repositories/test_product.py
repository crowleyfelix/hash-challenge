from motor.motor_asyncio import AsyncIOMotorClient
from app.tasks import FixturesTask
from app.repositories.mongodb import ProductRepository
from tests.base import BaseTestCase, async_test

class TestProductRepository(BaseTestCase):
    async def setUpAsync(self):
        await super().setUpAsync()
        self.fixtures = FixturesTask()
        await self.fixtures.execute()
        client = AsyncIOMotorClient("mongodb://mongodb:27017",
                                     uuidRepresentation="standard",
                                     connect=False)

        self.repo = ProductRepository(client.mgm_lab)
    
    async def tearDownAsync(self):
        await self.fixtures.revert()

    @async_test
    async def test_list(self):
        products = await self.repo.list({"limit": 100})
        for expected in self.fixtures.products:
            actual = next((p for p in products if p.id == expected["id"]), None)
            self.assertEqual(actual, expected)