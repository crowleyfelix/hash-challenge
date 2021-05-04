"""Módulo da aplicação web."""
from gunicorn.app.base import BaseApplication as GunicornBaseEngine
from sanic import Sanic
from app import application
from app.infrastructure import logging, ioc


class WebServerTask(GunicornBaseEngine):

    GUNICORN_STDOUT = "-"

    def __init__(self, app):
        self.app = app
        GunicornBaseEngine.__init__(self)

    def execute(self):
        GunicornBaseEngine.run(self)

    def load_config(self):
        config = self.app.config

        config = {
            "bind": f"{config.server.host}:{config.server.port}",
            "accesslog": self.GUNICORN_STDOUT,
            "errorlog": self.GUNICORN_STDOUT,
            "capture_output": True,
            "loglevel": config.log.access_level,
            "access_log_format": logging.FORMATTERS["access"]["format"],
            "worker_class": "sanic.worker.GunicornWorker",
            "workers": config.server.workers
        }

        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        server = Sanic(__name__)
        server.before_server_start(self.on_server_start)
        server.after_server_stop(self.on_server_stop)
        return server

    async def on_server_start(self, *args, **kwargs):
        self.app.loop = asyncio.get_event_loop()
        await self.app.setup()

    async def on_server_stop(self, *args, **kwargs):
        await self.app.shutdown()

if __name__ == "__main__":
    app = application.build()

    task = WebServerTask(app)
    task.execute()