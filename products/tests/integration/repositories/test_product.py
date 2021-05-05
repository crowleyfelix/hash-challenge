from app.repositories.mongodb import ProductRepository
from tests.base import BaseTestCase, async_test

class TestProductRepository(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.repo = ProductRepository()
    
    @async_test
    async def test_list(self):
        products = await self.repo.list({"limit": 100})
        for expected in self.fixtures.products:
            actual = next((p for p in products if p.id == expected["id"]), None)
            expected["discount"] = None
            self.assertEqual(actual.dict(), expected)

