from tests.base import BaseTestCase, async_test


class TestProductsRoute(BaseTestCase):
    @async_test
    async def test_list(self):
        req, resp = await self.app.server.asgi_client.get(f"/users/{self.fixtures.users[1]['id']}/products")
        self.assertEqual(resp.status_code, 200)

        for product in resp.json["data"]:
            self.assertIsNotNone(product["discount"])
