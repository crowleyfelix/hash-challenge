from motor.motor_asyncio import AsyncIOMotorClient
from app.repositories.mongodb import ProductRepository
from tests.base import BaseTestCase, async_test

class TestProductRepository(BaseTestCase):
    def setUp(self):
        super().setUp()
        client = AsyncIOMotorClient("mongodb://mongodb:27017",
                                     uuidRepresentation="standard",
                                     connect=False)

        self.repo = ProductRepository(client.mgm_lab)
    
    @async_test
    async def test_list(self):
        print(await self.repo.list({}))