from sanic import json, Request
from app.infrastructure import ioc

async def list_products(request: Request, user_id):
    svc = ioc.instance(ioc.Dependencies.product_svc)
    result = await svc.list(user_id, dict(request.query_args))
    return json(result.dict())