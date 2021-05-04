from sanic import json, Request
from app.infrastructure import ioc

async def list_products(request: Request):
    svc = ioc.instance(ioc.Dependencies.product_svc)
    products = await svc.list(request.query_args)
    return json([p.dict() for p in products])