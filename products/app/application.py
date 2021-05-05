"""Módulo da aplicação web."""
import logging
import asyncio
import grpc.aio
from sanic import Sanic
from motor.motor_asyncio import AsyncIOMotorClient
from app import repositories, services
from app.infrastructure import ApplicationConfig, ioc
from proto.discounts_pb2_grpc import DiscountCalculatorStub


logger = logging.getLogger(__name__)


def build(server, loop=None):
    config = ApplicationConfig()
    return _Application(server, config, loop)


class _Application:
    def __init__(self, server, config, loop=None):
        self.server: Sanic = server
        self.config = config
        self.loop = loop or asyncio.get_event_loop()

    async def setup(self):
        try:
            logger.debug("Creating new application")

            ioc.configure(self._configure_deps)

        except Exception as ex:
            logger.error(f"Error: {ex}")
            raise

    def _configure_deps(self, binder):
        mongodb = AsyncIOMotorClient(self.config.mongodb.uri,
                                     uuidRepresentation="standard",
                                     connect=False)

        binder.bind(ioc.Dependencies.server, self.server)
        binder.bind(ioc.Dependencies.config, self.config)
        binder.bind(ioc.Dependencies.loop, self.loop)
        binder.bind(ioc.Dependencies.mongodb_driver, mongodb)
        binder.bind_to_provider(ioc.Dependencies.product_repo, lambda: repositories.ProductRepository())
        binder.bind_to_provider(ioc.Dependencies.product_svc, lambda: services.ProductService())
        binder.bind_to_provider(ioc.Dependencies.discounts_api, lambda: DiscountCalculatorStub(
            grpc.aio.insecure_channel(f"{self.config.discounts_api.host}:{self.config.discounts_api.port}")))

    async def shutdown(self):
        logger.info("Shutting down application")
        await ioc.dispose()
