import functools
import asyncio
from unittest import TestCase
import json
from sanic import Sanic
from sanic_testing import TestManager
from app import application, routes
from app.tasks import FixturesTask
from app.infrastructure import sanic

server = Sanic(__name__)
server.error_handler = sanic.CustomErrorHandler()
TestManager(server)
routes.register(server)

def async_test(func, *args, **kwargs):
    @functools.wraps(func, *args, **kwargs)
    def new_func(self, *inner_args, **inner_kwargs):
        return self.loop.run_until_complete(
            func(self, *inner_args, **inner_kwargs))

    return new_func


class BaseTestCase(TestCase):
    maxDiff = 2048

    def setUp(self, *args):
        self.loop = asyncio.get_event_loop()
        self.app = application.build(server, self.loop)
        self.fixtures = FixturesTask()
        super().setUp()
        self.loop.run_until_complete(self.setUpAsync())

    def tearDown(self, *args):
        self.loop.run_until_complete(self.tearDownAsync())
        super().tearDown()

    async def setUpAsync(self):
        await self.app.setup()
        await self.fixtures.execute()

    async def tearDownAsync(self):
        await self.app.shutdown()
        await self.fixtures.revert()

    def async_return(self, result) -> asyncio.Future:
        f = asyncio.Future()
        f.set_result(result)
        return f

    def async_raise(self, ex):
        async def wrap(*args, **kwargs):
            raise ex
        return wrap

    def assertObjectsEqual(self, first, second):
        first = json.dumps(first)
        second = json.dumps(second)
        first = json.loads(first)
        second = json.loads(second)

        self.assertEqual(first, second)
