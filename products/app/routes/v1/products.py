from sanic import json, Request
from app.infrastructure import ioc

async def list_products(request: Request):
    svc = ioc.instance(ioc.Dependencies.product_svc)

    return json(await svc.list(request.query_args))