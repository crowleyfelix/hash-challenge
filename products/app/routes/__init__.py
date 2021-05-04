from sanic import Sanic
from . import v1


def register(server: Sanic):
    server.add_route(v1.list_products, "/info")
