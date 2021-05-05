from tests.base import BaseTestCase, async_test


class TestProductsRoute(BaseTestCase):
    @async_test
    async def test_list(self):
        req, resp = await self.app.server.asgi_client.get("/users/1/products")
        self.assertEqual(resp.status_code, 200)
