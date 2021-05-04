"""Módulo da aplicação web."""
import logging
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app import repositories, services
from app.infrastructure import ApplicationConfig, ioc


logger = logging.getLogger(__name__)


def build(loop=None):
    config = ApplicationConfig()
    return _Application(config, loop)


class _Application:
    def __init__(self, config, loop=None):
        self._config = config
        self._loop = loop or asyncio.get_event_loop()

    @property
    def config(self) -> ApplicationConfig:
        return self._config

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        return self._loop

    async def setup(self):
        try:
            logger.debug("Creating new application")

            ioc.configure(self._configure_deps)

        except Exception as ex:
            logger.error(f"Error: {ex}")
            raise

    def _configure_deps(self, binder):
        mongodb = AsyncIOMotorClient(self._config.mongodb.uri,
                                     uuidRepresentation="standard",
                                     connect=False)

        binder.bind(ioc.Dependencies.config, self._config)
        binder.bind(ioc.Dependencies.loop, self._loop)
        binder.bind(ioc.Dependencies.mongodb_driver, mongodb)
        binder.bind_to_provider(ioc.Dependencies.product_repo, lambda: repositories.ProductRepository())
        binder.bind_to_provider(ioc.Dependencies.product_svc, lambda: services.ProductService())

    async def shutdown(self):
        logger.info("Shutting down application")
        await ioc.dispose()
