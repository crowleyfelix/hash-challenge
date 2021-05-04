from app.infrastructure import ioc

class ProductService:
    async def list(self, filters):
        repo = ioc.instance(ioc.Dependencies.product_repo)
        return await repo.list(filters)